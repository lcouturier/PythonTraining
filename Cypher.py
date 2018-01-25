def next_letter(c, key):
    if ord(c) + key <= 90:
        return chr((ord(c) + key))

    return chr((((ord(c) + key) - 90) + 65) - 1)

def cipher_wheel(phrase, key):
    result = ""
    for c in phrase.upper():
        if c != " ":
            result = result + next_letter(c, key)
        else:
            result = result + c
    return result
