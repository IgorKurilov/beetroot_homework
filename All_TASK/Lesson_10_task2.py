def outer_function():
    def inner_function():
        print("This is the inner function")

    return inner_function

# Accessing the inner function
inner = outer_function()
inner()  # This will print "This is the inner function"
