structured_output_translation = {
    "name": "translation",
    "description": "Translate the word into its equivalents in different languages.",
    "input_schema": {
        "type": "object",
        "properties": {
            "original_language": {
                "type": "string",
                "description": "The original query or word.",
            },
            "arabic": {
                "type": "string",
                "description": "The original query or word translated to Arabic.",
            },
            "french": {
                "type": "string",
                "description": "The original query or word translated to French.",
            },
            "vietnamese": {
                "type": "string",
                "description": "The original query or word translated to Vietnamese.",
            },
        },
        "required": ["original_language"],  # Optional but recommended
    },
}
