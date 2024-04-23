# Initialize lists to store all integers and those meeting the condition
all_integers = []
divisible_by_7_not_multiple_of_5 = []

# Generate a list containing all integers from 1 to 100
num = 1
while num <= 100:
    all_integers.append(num)
    num += 1

# Iterate through the list of all integers and check the condition
index = 0
while index < len(all_integers):
    if all_integers[index] % 7 == 0 and all_integers[index] % 5 != 0:
        divisible_by_7_not_multiple_of_5.append(all_integers[index])
    index += 1

# Print the list of integers meeting the condition
print(divisible_by_7_not_multiple_of_5)