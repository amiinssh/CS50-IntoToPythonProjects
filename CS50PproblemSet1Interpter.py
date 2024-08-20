def main():

    expression = input("Expression: ").strip()

    parts = expression.split()

    if len(parts) != 3:
        print("Error: Invalid input format.")
        return

    try:
        x = int(parts[0])
        operator = parts[1]
        z = int(parts[2])
    except ValueError:
        print("Error: Invalid numbers.")
        return

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':

        if z == 0:
            print("Error: Division by zero.")
            return

        result = x / z
    else:
        print("Error: Invalid operator.")
        return

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
