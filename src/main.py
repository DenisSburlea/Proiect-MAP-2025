from random import shuffle #pentru a genera un alfabet aleator
from pathlib import Path  #pentru a lucra cu cai de fisiere
import secrets #pentru a genera chei sigure
import argparse #pentru a lucra cu argumente din linia de comanda

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


def frequence(text):
    english_freq = "etaoinsrhdlucmfywgpbvkxqjz" #cele mai frecvente litere in limba engleza
    vowels = "aeiou" #vocalele in limba engleza     
    scor = 0 #scor de frecventa

    for char in text.lower():
        if char in english_freq[:12]: #primele 12 litere cele mai frecvente
            scor += 3
        elif char in english_freq[:18]: #primele 18 litere cele mai frecvente
            scor += 2
        else: #litere mai putin frecvente
            scor -= 3
        
        if char in vowels: #bonus pentru vocale
            scor += 2
            
    return scor

def caesar_brute_force(text):
    best_scor = -1
    best_decrypt = ""
    best_shift = 0
    output = "" 

    for key in range(26): #incercam toate cele 26 de deplasari posibile 
        decrypted = caesar_decrypt(text,key)
        scor = frequence(decrypted)
        
        output += f"Shift {key}: {decrypted}\n"

        if scor > best_scor: #daca gasim un scor mai bun, actualizam best-urile
            best_scor = scor
            best_decrypt = decrypted
            best_shift = key
            
    output += f'\nRezultat posibil: "{best_decrypt}" cu deplasament {best_shift}' #cea mai probabila decriptare
    return output

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


def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()


def write_file(filepath,text, append=False):
    mode = "a" if append else "w"
    with open(filepath, mode) as f:
        f.write(text)


def generate_key(length):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = ""
    for _ in range(length):
        key += secrets.choice(alphabet)
    
    return key

def main():
    parser = argparse.ArgumentParser(description = "Cryptography App")

    #adaugare de argumente
    parser.add_argument("action", nargs = "?", 
                        choices=["encrypt", "decrypt"], 
                        help = "Actiune de criptare/decriprare") 
    
    parser.add_argument("text", nargs = "?", 
                        help = "Text de criptat/decriptat")
    
    parser.add_argument("--algo", choices=["caesar", "vigenere", "substitutie", "xor"],
                         help = "Algoritm")
    
    parser.add_argument("--key", 
                        help = "Cheie pentru algoritm")

    parser.add_argument("--file", 
                        help = "Fiser de intrare")

    parser.add_argument("--output", 
                        help = "Fisier de iesire")

    parser.add_argument("--brute_force", 
                        help = "Brute force pentru Caesar")
    
    parser.add_argument("--generate_key", 
                        action = "store_true", 
                        help = "Generare cheie sigura")
    
    parser.add_argument("--length", 
                        type=int,
                        help="Lungimea cheii")
    
    parser.add_argument("--count",
                        type=int,
                        default=1,
                        help="Numar de chei de generat")

    args = parser.parse_args()

    #gestionare generare chei
    if args.generate_key:
        length = args.length if args.length else 16
        count = args.count if args.count else 1

        if args.output:
            for _ in range(count):
                key = generate_key(length)
                write_file(args.output, key + "\n", append=True)
            print(f"{count} chei generate si salvate in fisierul {args.output}")
        else:
            for _ in range(count):
                key = generate_key(length)
                print(key)

        return
    
    #gestionare brute force Caesar
    if args.brute_force:
        if args.algo and args.algo != "caesar":
            print("Brute force este disponibil doar pentru algoritmul Caesar.")
            return
        
        text = caesar_brute_force(args.brute_force)

        if args.output:
            write_file(args.output, text)
            print(f"Rezultatul a fost salvat in fisierul {args.output}")
        else:
            print(text)
        return
    
    #daca nu s-a specificat actiunea, afisam help-ul
    if not args.action:
        parser.print_help()
        return
    
    
    if not args.file and not args.text:
        print("Trebuie sa specifici fie fisier de input fie text.")
        return
    
    input_text = read_file(args.file) if args.file else args.text #citim textul de intrare din fisier sau din linia de comanda

    if args.algo == "caesar": #gestionare algoritm Caesar
        key = int(args.key) if args.key else 3
        result = caesar(input_text,key) if args.action == "encrypt" else caesar_decrypt(input_text,key)

    elif args.algo == "vigenere": #gestionare algoritm Vigenere
        if not args.key:
            print("Cheia este necesara pentru algoritmul Vigenere.")
            return
        
        result = vigenere(input_text,args.key) if args.action == "encrypt" else vigenere_decrypt(input_text,args.key)

    elif args.algo == "substitutie": #gestionare algoritm Substitutie
        if args.key:
            if len(args.key) != 26:
                print("Cheia pentru substitutie trebuie sa aiba 26 de caractere.")
                return
            key = args.key
        else:
            key = ''.join(alfabet_aleator())
            print(f"Alfabetul aleator generat: {key}")
        
        result = substitutie(input_text,key) if args.action == "encrypt" else substitutie_decrypt(input_text,key)

    elif args.algo == "xor": #gestionare algoritm XOR
        if not args.key:
            print("Cheia este necesara pentru algoritmul XOR.")
            return
        if args.action == "encrypt":
            resultxor = xor(input_text,args.key)
            result = base64_encode(resultxor)
        else:
            resultdecode = base64_decode(input_text)
            result = xor(resultdecode,args.key)

    if args.output: #salvare rezultat in fisier sau afisare in consola
        write_file(args.output, result)
        print(f"Rezultatul a fost salvat in fisierul {args.output}")
    else:
        print(result)
    

if __name__ == "__main__":
    main()