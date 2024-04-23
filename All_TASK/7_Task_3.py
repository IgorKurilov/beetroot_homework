# writen by  Igor Kurilov
import random

# Read input string
input_string = input("Enter a string: ")

# Generate and print 5 random strings
for _ in range(5):
    random_string = ''.join(random.sample(input_string, len(input_string)))
    print(random_string)