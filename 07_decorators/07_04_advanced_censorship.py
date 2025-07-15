# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor(*bad_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            for word in bad_words:
                censored = word[0] + "*" * (len(word) - 1)
                text = text.replace(word, censored)
                text = text.replace(word.capitalize(), censored)
            return text
        return wrapper
    return decorator

@censor("shoot", "crab", "fuck", "heck")
def say_something():
    return "Fuck, I bumped my toe! Shoot! That hurt like the heck! Crab!"

print(say_something())