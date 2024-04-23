# Створення списку з днями тижня
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Створення словника {1: "Monday", 2: "Tuesday", ...}
days_dict = {index + 1: day for index, day in enumerate(week_days)}

# Створення зворотнього словника {"Monday": 1, "Tuesday": 2, ...}
reverse_days_dict = {day: index + 1 for index, day in enumerate(week_days)}

# Виведення результатів
print("Словник днів тижня:")
print(days_dict)

print("\nЗворотний словник днів тижня:")
print(reverse_days_dict)