import anthropic
import dotenv
import os
from tools.tool_definitions import tool_definition
from tools.calculator import calculator

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the API key from the environment variables
api_key = os.environ.get("ANTHROPIC-API-KEY")

# Create an Anthropic client instance with the API key
client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    system="You have access to tools, but only use them when necessary.  If a tool is not required, respond as normal",
    messages=[
        {
            "role": "user",
            "content": "What color are emeralds?",
        }
    ],
    tools=[tool_definition],
)

name = response.content[1].name
print(name)
operation_tools = response.content[1].input

operation = operation_tools["operation"]
operand1 = operation_tools["operand1"]
operand2 = operation_tools["operand2"]

result = calculator.calculator(operation, int(operand1), int(operand2))
print(result)
