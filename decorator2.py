def stop_words(words):
    def decorator(func):
        def wrapper(name):
            slogan = func(name)
            for word in words:
                slogan = slogan.replace(word, '*')
            return slogan
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

# Test the decorated function
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
