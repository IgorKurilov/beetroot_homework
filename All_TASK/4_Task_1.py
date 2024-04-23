def get_first_last_two_chars(input_str):
    if len(input_str) < 2:
        return ""  # Return empty string if the length is less than 2
    else:
        return input_str[:2] + input_str[-2:]  # Concatenate first 2 and last 2 characters


# Test cases
sample_strings = ['helloworld', 'my', 'x']
for sample in sample_strings:
    print(f"Sample String: '{sample}'")
    print("Expected Result:", get_first_last_two_chars(sample))