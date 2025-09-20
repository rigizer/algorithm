import sys
input = lambda: sys.stdin.readline().rstrip()

def split_words(style, name):
    if style == 2:
        return name.split('_')
    else:
        words = []
        start = 0
        for i, ch in enumerate(name):
            if ch.isupper() and i > 0:
                words.append(name[start:i].lower())
                start = i
        words.append(name[start:].lower())
        return words

def to_camel(words):
    return words[0] + ''.join(w.capitalize() for w in words[1:])

def to_snake(words):
    return '_'.join(words)

def to_pascal(words):
    return ''.join(w.capitalize() for w in words)

style, name = input().split()
style = int(style)

words = split_words(style, name)

print(to_camel(words))
print(to_snake(words))
print(to_pascal(words))