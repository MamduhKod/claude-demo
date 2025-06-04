import anthropic
import dotenv
import os
from tools import calculator, tool_definitions, wiki

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the API key from the environment variables
api_key = os.environ.get("ANTHROPIC-API-KEY")

# Create an Anthropic client instance with the API key
client = anthropic.Anthropic(api_key=api_key)


def ask_claude(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=500,
        system="You have access to tools, but only use them when necessary.  If a tool is not required, respond as normal",
        messages=messages,
        tools=[tool_definitions.calculator_tool],
    )

    if response.stop_reason == "tool_use":
        tool_use = response.content[-1]
        tool_name = tool_use.name
        tool_input = tool_use.input

        if tool_name == "calculator":
            print("Claude wants to use the calculator tool")
            operand = tool_input["operation"]
            operand1 = tool_input["operand1"]
            operand2 = tool_input["operand2"]

            try:
                result = calculator.calculator(operand, int(operand1), int(operand2))
                print("Calculation result is:", result)
                return result
            except ValueError as e:
                print(f"Error: {str(e)}")

    elif response.content == "end_turn":
        print("Claude didn't want to use a tool")
        print("Claude responded with:")
        print(response.content[0].text)
        return response


ask_claude("WHat is 500 times 234234?")


def get_research_help(title, n):
    messages = [{"role": "user", "content": f"Find {n} topics on research {title}"}]
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=500,
        system="You have access to tools, but only use them when necessary.  If a tool is not required, respond as normal",
        messages=messages,
        tools=[tool_definitions.wiki_tool],
    )

    if response.stop_reason == "tool_use":
        tool_use = response.content[-1]
        tool = tool_use.name
        topic = tool_use.input["research_topic"]
        titles = tool_use.input["article_titles"]
        if not titles:
            print("No article titles found.")
            return

        if isinstance(titles, str):
            # If it's a string, split it into a list by commas, and strip whitespace
            titles = [t.strip() for t in titles.split(",")]

        selected_titles = titles[:n]

        if tool == "wiki":
            try:
                print("Claude used wikipedia tool.")
                result = wiki.generate_wikipedia_reading_list(topic, selected_titles)
                print(
                    f"Generated reading list for {topic} with {len(selected_titles)} articles."
                )
                return result
            except ValueError as e:
                print(f"Error: {str(e)}")

    elif response.content == "end_turn":
        print("Claude didn't want to use a tool")
        print("Claude responded with:")
        print(response.content[0].text)


get_research_help("Drottningholm", 3)
