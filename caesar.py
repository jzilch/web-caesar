def alphabet_position(letter):
    for i in letter:
        if letter != i.upper():
            number = ord(i) - 97
        else:
            number = ord(i) - 65
        return number

def rotate_character(char, rot):
    for i in char:
        if char != char.upper() and char.isalpha():
            rotate = rot % 26
            new_char = alphabet_position(char) + rotate
            new_character = new_char % 26
            pos = new_character + 97
            return chr(pos)
        elif char != char.lower() and char.isalpha():
            rotate = rot % 26
            new_char = alphabet_position(char) + rotate
            new_character = new_char % 26
            pos = new_character + 65
            return chr(pos)
        elif char != char.isalpha():
            return char

def encrypt(text, rot):
    newtext = ""
    for char in text:
        if char.isalpha():
            newtext += rotate_character(char, rot)
        else:
            newtext += char
    return newtext
