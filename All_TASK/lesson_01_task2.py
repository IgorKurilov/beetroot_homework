def main():
    # Get input from the user
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))

    # Calculate the sum
    print(f"{a} + {b} = {a + b}")

    # Calculate the difference
    print(f"{a} - {b} = {a - b}")

    # Calculate the product
    print(f"{a} * {b} = {a * b}")

    # Calculate the division
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Cannot divide by zero!")

    # Calculate the exponentiation
    print(f"{a} ** {b} = {a ** b}")

    # Calculate the floor division
    if b != 0:
        print(f"{a} // {b} = {a // b}")
    else:
        print("Cannot perform floor division by zero!")

    # Calculate the modulus
    if b != 0:
        print(f"{a} % {b} = {a % b}")
    else:
        print("Cannot perform modulus operation by zero!")


if __name__ == "__main__":
    main()