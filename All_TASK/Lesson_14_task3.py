def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate type
            if not isinstance(args[0], type_):
                print(f"Argument '{args[0]}' is not of type '{type_.__name__}'")
                return False
            
            # Validate max_length
            if len(args[0]) > max_length:
                print(f"Length of argument '{args[0]}' exceeds maximum allowed length of {max_length}")
                return False
            
            # Validate contains
            for char in contains:
                if char not in args[0]:
                    print(f"Argument '{args[0]}' does not contain required character '{char}'")
                    return False
            
            # If all checks pass, call the original function
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# Testing the decorator
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
