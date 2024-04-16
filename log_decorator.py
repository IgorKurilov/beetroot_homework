# Декоратор log_decorator тепер є функцією, яка повертає справжній декоратор,
# який засікає час виконання.
#
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def first_decorator(func):
    def wrapper():
        print("falling asleep")
        func()
        print("wake up")
    return wrapper

def second_decorator(func):
    def wrapper():
        print("Second in")
        func()
        print("Second out")
    return wrapper
# Додано аргумент debug до функції log_decorator,
# який визначає, чи слід включити логування часу виконання.
def log_decorator(debug=False):
    def decorator(func):
        def wrapper():  # Внутрішній декоратор wrapper тепер реєструє час початку та 
            #             завершення виконання задекорованої функції та обчислює різницю між ними.
            # 
            start_time = time.time()
            if debug:
                logger.info(f"Execution started at {start_time}")
            func()
            end_time = time.time()
            if debug:
                logger.info(f"Execution ended at {end_time}")
                logger.info(f"Execution took {end_time - start_time} seconds")
        return wrapper
    return decorator

@log_decorator(debug=False)
def long_function():
    time.sleep(5)
    print("Inside the function")

# Логування відбувається тільки тоді, коли debug=True.
# можливо включати або виключати логування в залежності від потреб за допомогою аргументу debug.
@log_decorator(debug=True) 
def other_function():
    time.sleep(2)
    print("Another function")

if __name__ == "__main__":
    long_function()
    other_function()