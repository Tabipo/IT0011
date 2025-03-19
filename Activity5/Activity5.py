choice = ""
while choice != "Q" and choice != "q":
    print("Python Calculator")
    print("Choose mathematical operation: ")
    print("[D] - Division")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")
    choice = input("Enter your choice: ")

    def division():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("\nERROR: Cannot divide by zero\n")
        else:
            print("\nThe result is: ", num1 / num2, "\n")

    def exponentiation():
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        print("\nThe result is: ", num1 ** num2, "\n")

    def remainder():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("\nERROR: Cannot divide by zero\n")
        else:
            print("\nThe result is: ", num1 % num2, "\n")

    def summation():
        result = 0
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 < num1:
            print("\nERROR: The second number should be greater than the first number\n")
        else:
            while num1 <= num2:
                result += num1
                num1 += 1
            print("\nThe result is: ", result, "\n")

    if choice == "D" or choice == "d":
        division()
    elif choice == "E" or choice == "e":
        exponentiation()
    elif choice == "R" or choice == "r":
        remainder()
    elif choice == "F" or choice == "f":
        summation()