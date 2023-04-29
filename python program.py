def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        print(f"{num1:g} {'+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/'} {num2:g} = {result:g}")
        if input("Do you want to perform another calculation? (yes/no): ").lower() == 'no':
            break

calculator()
