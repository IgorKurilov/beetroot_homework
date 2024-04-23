# writen by igkurilov@gmail.com 
def make_operation(operator, *args):
    result = args[0] if args else 0  # Initialize result with the first argument or 0 if no arguments provided
    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num
    elif operator == '*':
        for num in args[1:]:
            result *= num
    return result

# Example usage:
print(make_operation('+', 7, 7, 2))  # Output: 16
print(make_operation('-', 5, 5, -10, -20))  # Output: 30
print(make_operation('*', 7, 6))  # Output: 42
