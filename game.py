import random
import time
import os
from grafik import bild
word = ""
leben = 8
word_list=[]
versuche = ""
entdeckt = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
def reset():
    global word, leben, versuche, entdeckt, word_list
    word = ""
    leben = 8
    versuche = ""
    entdeckt= []
    word_list=[]
    os.system('cls')
    print("Neues Spiel")
    spiel()

def datei_laden(path):
    try:
        with open(path, 'r') as file:
            lines = [line.strip().lower() for line in file.readlines()]
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"die Datei {path} wurde nicht gefunden.")


def select_sprache():
    global word_list
    done=False
    print("Willkommen beim Hangman")
    while not done:
        input_sprache = input("Wähle eine Sprache: Deutsch, Englisch oder Französisch: ").lower()
        if input_sprache == "deutsch":
            word_list = datei_laden(r'Python\hangman\words_de.txt')
            done = True
        elif input_sprache == "englisch":
            word_list = datei_laden(r'Python\hangman\words_en.txt')
            done = True
        elif input_sprache == "französisch":
            word_list = datei_laden(r'Python\hangman\words_fr.txt')
            done = True
        else:
            print("Ungültige Spracheingabe.")
            time.sleep(2)
            os.system('cls')
  
def frag_buchstabe():
    global versuche, leben
    done = False
    while not done:
        eingabe = input("Rate einen Buchstaben: ").lower()
        if eingabe == "":
            os.system('cls')
            print(bild(8-leben))
            print("Wort: " + " ".join(entdeckt))
            print("Bitte gib einen Buchstaben ein.")
        elif eingabe not in versuche:
            if len(eingabe) == 1 and eingabe.isalpha():
                versuche += eingabe
                done = True
            else:
                os.system('cls')
                print(bild(8-leben))
                print("Wort: " + " ".join(entdeckt))
                print(f"{eingabe} ist keine gültige Eingabe")

        else:
            os.system('cls')
            print(bild(8-leben))
            print("Wort: " + " ".join(entdeckt)) 
            print(f"Du hast {eingabe} schon probiert")        
    return eingabe

def in_wort(buchstabe):
    global entdeckt
    abzug = True
    if buchstabe in word:
        for i in range(len(word)):
            if buchstabe == word[i]:
                entdeckt[i] = buchstabe
                abzug = False
    return abzug
            
def logik():
    global entdeckt, versuche, word, leben
    os.system('cls')
    print(bild(8-leben))
    print("Wort: " + " ".join(entdeckt)) 
    while leben > 1:
        buchstabe = frag_buchstabe()
        if not in_wort(buchstabe):
            os.system('cls')
            print(bild(8-leben))
            print("Wort: " + " ".join(entdeckt)) 
            print(f"Richtig!")
        else:
            leben -= 1
            os.system('cls')
            print(bild(8-leben))
            print("Wort: " + " ".join(entdeckt)) 
            print(f"Falsch! Probiere es nochmals.")
        
        if "_" not in entdeckt:
            os.system('cls')
            print("Glückwunsch! Du hast das Wort erraten!")
            break
    else:
        os.system('cls')
        print(bild(8-leben))
        print(f"Game over! Das Wort war: {word}")
    time.sleep(0.1)
def spiel():
    global word, entdeckt, versuche
    select_sprache()
    word = random.choice(word_list).lower()
    entdeckt = ["_" for _ in word]
    versuche = ""
    logik()
    if input("Neues Spiel? (j/n): ").lower() == "j":
        reset()
    else: 
        print("Auf Wiedersehen!")
        exit()
spiel()