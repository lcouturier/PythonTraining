def next_letter(c, key):
    if ord(c) + key <= 90:
        return chr((ord(c) + key))

    return chr((ord(c) + key) - 26)


def previous_letter(c, key):
    if ord(c) - key >= 65:
        return chr((ord(c) - key))

    return chr((ord(c) - key) + 26)


def cipher_wheel_crypt(phrase, key):
    result = ""
    for c in phrase.upper():
        if c != " ":
            result = result + next_letter(c, key)
        else:
            result = result + c
    return result


def cipher_wheel_decrypt(phrase, key):
    result = ""
    for c in phrase.upper():
        if c != " ":
            result = result + previous_letter(c, key)
        else:
            result = result + c
    return result
