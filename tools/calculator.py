def calculator(operation, operand1, operand2):
    if operation == "add":
        return operand1 + operand2
    elif operation == "subtract":
        return operand1 - operand2
    elif operation == "multiply":
        return operand1 * operand2
    elif operation == "divide":
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 / operand2
    else:
        raise ValueError(f"Unsupported operation: {operation}")


calculator("add", 2, 3)
