import anthropic
import dotenv
import os
from SO import structured_output_translation
import json

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the API key from the environment variables
api_key = os.environ.get("ANTHROPIC-API-KEY")

# Create an Anthropic client instance with the API key
client = anthropic.Anthropic(api_key=api_key)


def get_translations(word: str):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4096,
        tools=[structured_output_translation],
        tool_choice={"type": "tool", "name": "translation"},
        messages=[{"role": "user", "content": word}],
    )

    response

    for content in response.content:
        print(content)
        if content.type == "tool_use" and content.name == "translation":
            result_json = json.dumps(content.input, indent=2, ensure_ascii=False)
            print(result_json)


get_translations("avocado")
