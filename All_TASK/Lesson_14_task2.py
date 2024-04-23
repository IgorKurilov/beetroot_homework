def stop_words(stop_words_list):
    def decorator(func):
        def wrapper(name):
            slogan = func(name)
            for word in stop_words_list:
                slogan = slogan.replace(word, '*')
            return slogan
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# Testing the decorator
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
