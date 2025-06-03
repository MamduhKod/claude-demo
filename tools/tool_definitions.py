from . import calculator
from .wiki import generate_wikipedia_reading_list

calculator_tool = {
    "name": "calculator",
    "description": "A simple calculator that performs basic arithmetic operations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"],
                "description": "The arithmetic operation to perform. Must be one of: add, subtract, multiply, divide.",
            },
            "operand1": {"type": "number", "description": "The first operand."},
            "operand2": {"type": "number", "description": "The second operand."},
        },
        "required": ["operation", "operand1", "operand2"],
    },
}

wiki_tool = {
    "name": "wiki",
    "description": "A tool for searching Wikipedia.",
    "input_schema": {
        "type": "object",
        "properties": {
            "research_topic": {
                "type": "string",
                "description": "The research topic to find articles about.",
            },
            "article_titles": {
                "type": "array",
                "description": "The titles of the researched articles.",
                "items": {
                    "type": "string",
                },
            },
        },
        "required": ["research_topic"],
    },
}


tool_functions = {"calculator": calculator, "wiki": generate_wikipedia_reading_list}
