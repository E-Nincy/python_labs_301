# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        offensive_words = ["shoot", "darn", "heck", "fuck", "shit", "damm"]
        for word in offensive_words:
            censored = word[0] + "*" * (len(word) - 1)
            text = text.replace(word, censored)
            text = text.replace(word.capitalize(), censored)
        return text
    return wrapper

@censor
def say_something():
    return "Fuck, i bumped my toe! Shoot! That hurt like heck!"

print(say_something())