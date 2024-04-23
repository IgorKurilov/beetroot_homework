def outer_function():
    def inner_function():
        print("This is the inner function!")

    # Returning the inner function
    return inner_function

# Assigning the returned function to a variable
my_function = outer_function()

# Calling the inner function
my_function()