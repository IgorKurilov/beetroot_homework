class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')

# Test
try:
    raise CustomException("Custom error message")
except CustomException as e:
    print("CustomException occurred:", e)