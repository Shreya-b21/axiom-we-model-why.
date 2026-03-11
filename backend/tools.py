# backend/tools.py

import re


def search_tool(query: str):

    database = {
        "capital of france": "Paris is the capital of France.",
        "president of france": "Emmanuel Macron is the president of France.",
    }

    q = query.lower()

    for key in database:
        if key in q:
            return database[key]

    return "No result found."


def calculator_tool(expression: str):

    try:
        # extract only numbers and math operators from the prompt
        cleaned = re.findall(r"[0-9+\-*/().]+", expression)

        math_expression = "".join(cleaned)

        result = eval(math_expression)

        return str(result)

    except Exception:
        return "Calculation failed."