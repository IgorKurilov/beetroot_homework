def count_local_variables(func):
    # Отримуємо словник локальних змінних для функції
    local_vars = func.__code__.co_varnames
    
    # Повертаємо кількість локальних змінних
    return len(local_vars)

# Приклад використання
def example_function():
    a = 10
    b = "hello"
    c = [1, 2, 3]
    return a + len(b) + len(c)

print("Кількість локальних змінних у функції 'example_function':", count_local_variables(example_function))
