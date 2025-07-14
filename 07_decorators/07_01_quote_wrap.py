# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def add_quotes(func):
    def wrapper(text):
        result = func(text)
        return f'"{result}"'
    return wrapper

@add_quotes
def say_something(text):
    return text

print(say_something("Hello World"))  
