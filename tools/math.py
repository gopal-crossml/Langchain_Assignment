from langchain.tools import tool

@tool
def math_calculator(expression: str) -> str:
    """
    Evaluates a simple mathematical expression.

    Input:
        expression (str): Example -> "(234 * 12) + 98"

    Output:
        str: Result of calculation
    """
    try:
        # Evaluate the expression
        result = eval(expression)

        return f"Result: {result}"

    except Exception as error:
        return f"Error evaluating expression: {error}"


