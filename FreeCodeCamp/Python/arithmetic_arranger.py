def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems is within the limit
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        # Split the problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check if operands are numeric
        if not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."

        # Check if the operator is valid
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Calculate the width of the line for the arranged problem
        width = max(len(num1), len(num2)) + 2

        # Format the operands and the operator
        line1 = num1.rjust(width)
        line2 = operator + ' ' + num2.rjust(width - 2)
        separator = '-' * width

        # Add the arranged problem to the list
        arranged_problems.append((line1, line2, separator))

    # If show_answers is True, calculate and add the answers
    if show_answers:
        answers = []
        for problem in problems:
            num1, operator, num2 = problem.split()
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answers.append(result.rjust(width))
        arranged_problems.append(answers)

    # Transpose the arranged problems if needed
    if show_answers:
        arranged_problems = [list(x) for x in zip(*arranged_problems)]

    # Combine the lines into a formatted string
    arranged_str = '\n'.join(['    '.join(line) for line in arranged_problems])

    return arranged_str

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

from arithmetic_arranger import arithmetic_arranger

print(
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# Run unit tests automatically
main(['-vv'])