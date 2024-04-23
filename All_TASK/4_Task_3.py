import random

def generate_question():
    """Generate a random mathematical expression."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    return expression

def evaluate_expression(expression):
    """Evaluate the given mathematical expression."""
    try:
        result = eval(expression)
        return result
    except:
        return None

def main():
    print("Welcome to the Math Quiz!")
    print("You'll be asked to solve a simple mathematical expression.")
    print("Let's get started!\n")

    while True:
        # Generate a random mathematical expression
        expression = generate_question()

        # Ask the user to solve the expression
        print("What is the result of:", expression)
        user_answer = input("Your answer: ")

        # Evaluate the expression and check user's answer
        correct_answer = evaluate_expression(expression)
        if correct_answer is not None:
            if user_answer == str(correct_answer):
                print("Congratulations! Your answer is correct.")
            else:
                print(f"Sorry, the correct answer is {correct_answer}.")
        else:
            print("Invalid expression. Please try again.")

        # Ask if the user wants to continue
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing the Math Quiz!")

if __name__ == "__main__":
    main()