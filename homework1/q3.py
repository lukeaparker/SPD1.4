# Given a string, find and return any duplicate characters.


pattern = "aabcddefg"
def dup(pattern):
    once = []
    twice = []
    for char in pattern:
        if char in once:
            if char in twice:
                continue
            twice.append(char)
        if char not in once:
            once.append(char)
    print(twice)
    return twice
dup(pattern)




