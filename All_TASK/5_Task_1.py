import random

# Generate a list of 10 random numbers
random_numbers = []
count = 0
while count < 10:
    random_numbers.append(random.randint(1, 100))  # Assuming range is from 1 to 100
    count += 1

# Find the largest number using a while loop
max_number = random_numbers[0]  # Initialize max_number with the first element
index = 1
while index < len(random_numbers):
    if random_numbers[index] > max_number:
        max_number = random_numbers[index]
    index += 1

# Print the list of random numbers and the largest number
print("List of random numbers:", random_numbers)
print("The greatest number:", max_number)