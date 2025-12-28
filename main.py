from random import shuffle #pentru a genera un alfabet aleator

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


def caesar_decrypt(text, key):     #la fel ca la criptare, insa scadem cheia
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


def caesar_brute_force(text):
    for key in range(0,26): #incercam toate cele 26 de chei posibile
        print("Shift ", key, ": ", caesar_decrypt(text, key))


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


def alfabet_aleator():    #functie pentru generare de alfabet aleator
    alf = list("abcdefghijklmnopqrstuvwxyz")
    shuffle(alf)
    return alf


def substitutie(text,alf):
    rez = ""

    for char in text:
        if char.islower():
            index = ord(char) - ord('a')  #calculam indexul literei in alfabetul normal
            rez += alf[index] #adaugam litera din alfabetul aleator la rezultat
        elif char.isupper():
            index = ord(char) - ord('A') #la fel ca la litere mici
            rez += alf[index].upper()
        else:
            rez += char
    return rez


def substitutie_decrypt(text,alf):
    rez = ""

    for char in text:
        if char.islower():
            index = alf.index(char)  #aflam indexul literei in alfabetul aleator 
            rez += chr(index + ord('a'))  #adaugam litera din alfabetul normal la rezultat
        elif char.isupper(): 
            index = alf.index(char.lower()) #la fel ca la litere mici
            rez += chr(index + ord('A'))
        else:
            rez += char
    return rez


def xor(text, key):
    rez = ""
    j = 0

    for char in text:
        charnou = chr(ord(char) ^ ord(key[j]))  #aplicam XOR intre codul ASCII al caracterului si cel al caracterului din cheie
        rez += charnou
        j += 1   
        if j == len(key):  #daca am ajuns la finalul cheii, resetam indexul
            j = 0
    return rez


def base64_encode(text):
    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" #alfabetul codarii Base64
    rez = ""
    string_binar = ""

    for char in text:
        string_binar += format(ord(char), '08b') #transformam fiecare caracter in binar pe 8 biti si adaugam la o variabila
    
    while len(string_binar) % 6 != 0:  #adaugam 0 ca si padding daca lungimea nu e multiplu de 6
        string_binar += "0"

    for i in range(0, len(string_binar), 6):  
        segment = string_binar[i:i+6] #impartim sirul binar in segmente de cate 6 biti
        index = int(segment,2)   #transformam segmentul din baza 2 (binar) in baza 10 (int)
        rez += base64_alphabet[index]  #adugam caracterul corespunzator din alfabetul Base64 la rez
    
    while len(rez) % 4 != 0: #adaugam '=' ca si padding daca lungimea nu e multiplu de 4
        rez += "="
    
    return rez

def base64_decode(text):
    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    rez = ""
    string_binar = ""

    text = text.replace("=", "")  #inalturam padding-ul

    for char in text:
        index = base64_alphabet.index(char)  #aflam indexul fiecarul caracter din text
        string_binar += format(index, '06b') #transformam indexul in binar pe 6 biti si adaugam la o variabila
    
    for i in range(0, len(string_binar), 8):  
        segment = string_binar[i:i+8] #impartim sirul binar in segmente de cate 8 biti
        rez += chr(int(segment,2)) #transformam segmentul din baza 2 (binar) in caracter
    
    return rez
#test
print("Caesar test:")
print(caesar("Hello, World!", 3))
print(caesar("Hello, World!", 50))

print(caesar_decrypt("Khoor, Zruog!", 3))
print(caesar_decrypt("Fcjjm, Umpjb!", 50))

print("\nCaesar brute force test:")
caesar_brute_force("Khoor, Zruog!")


print("\nVigenere test:")
print(vigenere("Hello, World!", "key"))
print(vigenere_decrypt("Rijvs, Uyvjn!", "key"))


print("\nSubstitutie test:")
alf = alfabet_aleator()
print("Alfabet standard: abcdefghijklmnopqrstuvwxyz")
print("Alfabet aleator:", ''.join(alf))
text_criptat = substitutie("Hello,World!", alf)
print(text_criptat)
print(substitutie_decrypt(text_criptat, alf))


print("\nXOR test (fara Base64):")
criptat = xor("Hello,World!", "key")
print(criptat)
decriptat = xor(criptat, "key")
print(decriptat)

print("\nXOR test (cu Base64):")
print(base64_encode(criptat))
print(base64_decode(base64_encode(criptat)))