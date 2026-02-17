def calculate(expression):
    numbers = []      # stack for numbers
    operators = []    # stack for operators

    # applies the last operator to the last two numbers
    def apply_operator():
        right = numbers.pop()
        left = numbers.pop()
        operator = operators.pop()

        if operator == '+':
            numbers.append(left + right)
        elif operator == '-':
            numbers.append(left - right)
        elif operator == '*':
            numbers.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError
            numbers.append(left / right)

    # operator precedence
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    i = 0
    while i < len(expression):
        char = expression[i]

        # read a full number (including decimals)
        if char.isdigit() or char == '.':
            number = ""
            while i < len(expression) and (
                expression[i].isdigit() or expression[i] == '.'
            ):
                number += expression[i]
                i += 1
            numbers.append(float(number))
            continue

        # opening bracket
        if char == '(':
            operators.append(char)

        # closing bracket
        elif char == ')':
            while operators[-1] != '(':
                apply_operator()
            operators.pop()  # remove '('

        # operator
        elif char in precedence:
            while (
                operators and
                operators[-1] in precedence and
                precedence[operators[-1]] >= precedence[char]
            ):
                apply_operator()
            operators.append(char)

        i += 1

    # apply remaining operators
    while operators:
        apply_operator()

    return numbers[0]


print("=== EASY CALCULATOR ===")
print("Allowed: +  -  *  /  ( )")
print("Type 'exit' to quit")

while True:
    user_input = input("\nEnter expression: ").replace(" ", "")

    if user_input.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        result = calculate(user_input)
        print("Result:", result)
    except:
        print("Invalid expression")
