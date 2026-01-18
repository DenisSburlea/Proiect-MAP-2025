# Aplicatie pentru criptare/decriptare text
Aplicatie de criptografie in linia de comanda care permite criptarea, decriptarea, generarea de chei si atacuri brute-force folosind algoritmi clasici.

## Autor
- **Nume:** Sburlea Irinel-Denis
- **Grupă:** AC-INFO-GRUPA 3.1  
- **Email:** irinel-denis.sburlea@student.upt.ro
- **An academic:** 2025-2026

## Descriere
 Aceasta aplicatie ofera o interfata de tip command-line pentru criptarea si decriptarea textului folosind algoritmi clasici precum Caesar, Vigenère, Substitutie si XOR. De asemenea, include functionalitati de generare de chei sigure si atac brute-force pentru cifrul Caesar.

 Aplicatia este utila pentru studentii care doresc sa inteleaga functionarea algoritmilor de criptografie, manipularea fisierelor si procesarea argumentelor din linia de comanda in Python.

## Tehnologii folosite
- **Limbaj:** Python 3.10+
- **Biblioteci:**
    - argparse - procesarea argumentelor din linia de comanda
    - pathlib - gestionarea portabila a cailor de fisiere
    - secrets - generarea de chei sigure
    - random - generarea alfabetului aleator pentru algoritmul de substitutie
- **Tools:** Git, Docker, GitHub Actions

## Cerințe sistem
- Python 3.10+
- Sistem de operare: Windows/Linux/macOS
- Nu sunt necesare dependente externe. Aplicatia foloseste doar biblioteca standard Python.

## Instalare
```bash
# Clone repository
git clone https://github.com/DenisSburlea/Proiect-MAP-2025.git
cd Proiect-MAP-2025
```

## Rulare
```bash
# Comandă de bază
./main.py --help 
```

## Exemple de comenzi

### Exemplul 1: Criptare Caesar
```bash
$ ./main.py encrypt "hello world" --algo caesar --key 3
Output: "khoor zruog"
```

### Exemplul 2: Decriptare Caesar din fisier
```bash
$ ./main.py decrypt --file input.txt --algo caesar --key 3 --output output.txt
Output: "Rezultatul a fost salvat in fisierul output.txt"
```

### Exemplul 3: Criptare Vigenère
```bash
$ ./main.py encrypt "secret message" --algo vigenere --key KEY
Output: "ciabir wiqceeo"
```

### Exemplul 4: Brute-Force Caesar
```bash
$ ./main.py --brute_force "khoor zruog"
Output(prescurtat): "Shift 0: khoor zruog
Shift 1: jgnnq yqtnf
...
Rezultat posibil: "ebiil tloia" cu deplasament 6"
```

### Exemplul 5: Generare chei sigure
```bash
$ ./main.py --generate_key --length 16 --count 5 --output keys.txt
Output: "5 chei generate si salvate in fisierul keys.txt"
```

## Funcționalități implementate
    [x] Criptare si decriptare Caesar
    [x] Criptare si decriptare Vigenère
    [x] Criptare si decriptare Substitutie
    [x] Criptare si decriptare XOR (cu Base64)
    [x] Brute-force pentru Caesar
    [x] Generare chei sigure
    [x] Citire si scriere din/in fisiere
    [ ] Brute-force mai corect si consistent (pentru viitor)

## Structura proiectului
```bash
Proiect-MAP-2025/
├──.github/
│ └──workflows/
│  └──build.yaml
├── src/
│ └── main.py - aplicatia principala
├──  tests/
│ ├── input_encrypt.txt - fisier de intrare pentru criptare
│ └── input_decrypt.txt - fisier de intrare pentru decriptare
├── README.md
└── Dockerfile - Containerul permite rularea aplicatiei fara instalarea Python local.
```

## Decizie de design
 - **Argparse pentru CLI:** permite o interfara clara si extensibila pentru utilizator
 - **Pathlib pentru fisiere:** ofera compatibilitate cross-platform si elimina erorile legate de
    cai relative
 - **Separarea algoritmilor in functii:** face codul usor de citit, testat si extins

## Probleme întâlnite și soluții
 - **Problemă:** salvarea fisierelor in locatii gresite

   **Solutie:** folosirea ```pathlib.Path.resolve()``` si crearea explicita a directoarelor 

 - **Problemă:** scor incorect la brute-force pentru texte scurte

   **Solutie:** ajustarea functiei de frecventa cu ponderi si bonus pentru vocale

## Testare
Testarea a fost realizata manual prin rularea comenzilor CLI pentru:
 - fiecare algoritm
 - input din fisier si din linia de comanda
 - generare de chei
 - brute_force

## Docker
### Build imagine local
    docker build -t crypto-app .
### Build imagine direct din github
    docker build -t crypto-app https://github.com/DenisSburlea/Proiect-MAP-2025.git
### Rulare imagine
    docker run crypto-app --help
### Rulare imagine direct din Docker (fara a mai da build)
    docker run denissburlea/crpytography-app

# Resurse folosite
 - **Python Official Documentation**

   https://docs.python.org/3/

 - **argparse - Python Standard Library**

   https://docs.python.org/3/library/argparse.html

 - **pathlib - Python Standard Library**

   https://docs.python.org/3/library/pathlib.html

 - **Stack Overflow - diverse solutii si clarificari**

   https://stackoverflow.com

## Licență
  **MIT License**

## Contact
  **Pentru întrebări:** irinel-denis.sburlea@student.upt.ro