import anthropic
import dotenv
import os
import sys
import wikipedia

# Load environment variables from .env
dotenv.load_dotenv()
api_key = os.environ.get("ANTHROPIC-API-KEY")

# Set up Claude client
client = anthropic.Anthropic(api_key=api_key)

# Add project root to import custom tools
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Tool definition
get_article_tool = {
    "name": "get_article",
    "description": "Fetches Wikipedia articles.",
    "input_schema": {
        "type": "object",
        "properties": {
            "n_of_articles": {"type": "string", "description": "Optional"},
            "article_titles": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Article titles to retrieve",
            },
        },
        "required": ["article_titles"],
    },
}


def get_article(search_terms):
    article_list = []
    for term in search_terms:
        results = wikipedia.search(term)
        if not results:
            article_list.append(f"No Wikipedia results for '{term}'")
            continue
        try:
            page = wikipedia.page(results[0], auto_suggest=False)
            article_list.append(page.content[:3000])  # Claude prefers shorter input
        except Exception as e:
            article_list.append(f"Error loading '{term}': {e}")
    return article_list


# SYSTEM & QUESTION
system_prompt = """
You are a helpful assistant. You can optionally use the `get_article` tool to retrieve Wikipedia articles.
Only call the tool if you're missing up-to-date information.
"""
question = "Why is the sky blue and who won the last UEFA Euro?"

# Initial user message
messages = [{"role": "user", "content": f"<question>{question}</question>"}]

# Start loop
while True:
    response = client.messages.create(
        model="claude-3-opus-20240229",
        system=system_prompt,
        messages=messages,
        tools=[get_article_tool],
        max_tokens=1000,
    )

    print("\n--- CLAUDE RESPONSE ---")
    for block in response.content:
        if block.type == "text":
            print(block.text)

    # Check for tool use
    if response.stop_reason == "tool_use":
        tool_use = response.content[-1]  # Should be ToolUseBlock
        tool_name = tool_use.name
        tool_input = tool_use.input
        tool_use_id = tool_use.id

        # Append assistant message containing tool call
        messages.append({"role": "assistant", "content": response.content})

        if tool_name == "get_article":
            print("Claude wants to fetch Wikipedia articles...")

            try:
                articles = get_article(tool_input["article_titles"])

                tool_result = {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use_id,
                            "content": [
                                {"type": "text", "text": text} for text in articles
                            ],
                        }
                    ],
                }
                messages.append(tool_result)

            except Exception as e:
                print(f"Tool error: {e}")
                break

    elif response.stop_reason == "end_turn":
        # Claude gave final answer
        messages.append({"role": "assistant", "content": response.content})
        break

print("\n--- FINAL ANSWER ---")
for block in response.content:
    if block.type == "text":
        print(block.text)
