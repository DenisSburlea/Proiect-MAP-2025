def caesar(text, key):
    rez = ""
    key = key % 26 #pentru a nu depasi 26, acela fiind numarul de litere din alfabet

    for char in text:    #aplicam criptarea pentru fiecare caracter din textul initial
       
        if char.islower():           #pentru litere mici
            charnou = ord(char) + key   #adunam cheia la codul ASCII al caracterului
            if charnou > ord('z'):     #daca depaseste codul ASCII al literei 'z', scadem o rotatie de alfabet
                charnou -= 26
            rez += chr(charnou)    #adunam caracterul criptat la rezultat
        elif char.isupper():       #pentru litere mari
            charnou = ord(char) + key    #la fel ca la litere mici
            if charnou > ord('Z'):
                charnou -= 26
            rez += chr(charnou)
        else:                     #daca nu e litera, o pastram
            rez += char

    return rez


def caesardecrypt(text, key):     #la fel ca la criptare, insa scadem cheia
    rez = ""
    key = key % 26

    for char in text:

        if char.islower():
            charnou = ord(char) - key
            if charnou < ord('a'):
                charnou += 26
            rez += chr(charnou)
        elif char.isupper():
            charnou = ord(char) - key
            if charnou < ord('A'):
                charnou += 26
            rez += chr(charnou)
        else:
            rez += char
    return rez


def vigenere(text, key):
    rez = ""
    key = key.lower() #transformam cheia in litere mici
    j = 0 #index pentru cheie

    for char in text:
        if char.islower():
            shift = ord(key[j]) - ord('a') #calculul shift-ului pe baza literei din cheie
            charnou = ord(char) + shift #adunam shift-ul la codul ASCII al caracterului
            if charnou > ord('z'):
                charnou -= 26
            rez += chr(charnou)
            j += 1            #incementam indexul
            if j == len(key): #daca am ajung la finalul cheii, resetam indexul
                j = 0
        elif char.isupper():  #la fel ca la litere mici
            shift = ord(key[j]) - ord('a')
            charnou = ord(char) + shift
            if charnou > ord('Z'):
                charnou -= 26
            rez += chr(charnou)
            j += 1
            if j == len(key):
                j = 0
        else:           #daca nu e litera, o pastram
            rez += char
    return rez


def vigenere_decrypt(text, key):  #la fel ca la criptare, insa scadem shift-ul
    rez = ""
    key = key.lower()
    j = 0

    for char in text:
        if char.islower():
            shift = ord(key[j]) - ord('a')
            charnou = ord(char) - shift
            if charnou < ord('a'):
                charnou += 26
            rez += chr(charnou)
            j += 1
            if j == len(key):
                j = 0
        elif char.isupper():
            shift = ord(key[j]) - ord('a')
            charnou = ord(char) - shift
            if charnou < ord('A'):
                charnou += 26
            rez += chr(charnou)
            j += 1
            if j == len(key):
                j = 0
        else:
            rez += char
    return rez


#test
print("Caesar test:")
print(caesar("Hello, World!", 3))
print(caesar("Hello, World!", 50))

print(caesardecrypt("Khoor, Zruog!", 3))
print(caesardecrypt("Fcjjm, Umpjb!", 50))

print("\nVigenere test:")
print(vigenere("Hello, World!", "key"))
print(vigenere_decrypt("Rijvs, Uyvjn!", "key"))