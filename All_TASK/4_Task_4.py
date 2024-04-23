def main():
    # Store your name in lowercase
    stored_name = "igor"

    # Ask for user input
    user_name = input("Please enter your name: ")

    # Check if the lowercase version of user input matches the stored name
    if user_name.lower() == stored_name:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()