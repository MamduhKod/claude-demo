from . import calculator
from .wiki import generate_wikipedia_reading_list, get_article

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

get_article_tool = {
    "name": "get_article",
    "description": "A tool to retrieve one or more updated Wikipedia articles.",
    "input_schema": {
        "type": "object",
        "properties": {
            "n_of_articles": {
                "type": "string",
                "description": "Number of articles to retrieve.",
            },
            "article_titles": {
                "type": "array",
                "description": "The titles of the articles to retrieve.",
                "items": {
                    "type": "string",
                },
            },
        },
        "required": ["search_term"],
    },
}


tool_functions = {
    "calculator": calculator,
    "wiki": generate_wikipedia_reading_list,
    "get_article": get_article,
}
