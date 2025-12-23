def caesar(text, key):
    rez = ""

    while key > 26:
        key = key % 26

    for char in text:
       
        if char.islower():
            charnou = ord(char) + key
            if charnou > ord('z'):
                charnou -= 26
            rez += chr(charnou)
        elif char.isupper():
            charnou = ord(char) + key
            if charnou > ord('Z'):
                charnou -= 26
            rez += chr(charnou)
        else:
            rez += char

    return rez

print(caesar("Hello, World!", 3))
print(caesar("Hello, World!", 50))