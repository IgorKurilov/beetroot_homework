# writen by  Igor Kurilov
# Taking input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculating the next age
next_age = age + 1

# Printing the birthday greeting
print("Hello " + name + ", on your next birthday you'll be " + str(next_age) + " years.")