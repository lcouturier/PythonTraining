def cipher_wheel(phrase, key):
    result = ""
    for c in phrase.upper():
        if c != " ":
            if ord(c) + key <= 90:
                result = result + chr((ord(c) + key))
            else:
                result = result + chr((((ord(c) + key) - 90) + 65) - 1)
        else:
            result = result + c
    return result
