import random

# Generate the first list of random integers
list1 = []
count = 0
while count < 10:
    list1.append(random.randint(1, 10))  # Assuming range is from 1 to 10
    count += 1

# Generate the second list of random integers
list2 = []
count = 0
while count < 10:
    list2.append(random.randint(1, 10))  # Assuming range is from 1 to 10
    count += 1

# Find common integers without duplicates
common_numbers = []
index = 0
while index < len(list1):
    if list1[index] in list2 and list1[index] not in common_numbers:
        common_numbers.append(list1[index])
    index += 1

# Print the original lists and the list of common integers
print("First list:", list1)
print("Second list:", list2)
print("Common integers without duplicates:", common_numbers)