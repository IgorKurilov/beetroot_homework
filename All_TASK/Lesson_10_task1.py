def count_local_variables(func):
    # Get local variables before calling the function
    before_locals = locals().copy()
    # Call the function
    func()
    # Get local variables after calling the function
    after_locals = locals().copy()
    # Calculate the difference
    local_variables_count = len(after_locals) - len(before_locals)
    return local_variables_count

# Define a function to test
def test_function():
    a = 10
    b = "Hello"
    c = [1, 2, 3]

# Call the function and print the result
print("Number of local variables declared:", count_local_variables(test_function))