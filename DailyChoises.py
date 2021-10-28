import datetime
import time 
import locale 


def vraag5(): 
    print("Wat ga je doen na school?\n")
    print("a = Naar de stad.")
    print("b = Je gaat naar huis.")
    print("c = Je blijft op school.")
    antwoord5 = input()
    if antwoord5 == "a": 
        print("Lekker shoppen")
        exit()
    elif antwoord5 == "b": 
        print("Lekker naar huis gaan is ook fijn.")
        exit()
    elif antwoord5 == "c": 
        print("Waarom blijf je sws op school?")
        exit()
    else: 
        print("Kies: a, b of c")
        print(vraag5())
     
def vraag4(): 
    print("Wat ga je doen als je voor de school staat.")
    print("a = Naar de les lopen en optijd zijn.")
    print("b = Naar de kantine lopen en iets telaat komen.")
    print("c = omkeren en naar huis gaan.")
    antwoord4 = input()
    if antwoord4 == "a": 
        print("Goed zo.")
        print(vraag5())
    elif antwoord4 == "b": 
        print("Je moet dan wel opschieten.")
        print(vraag5())
    elif antwoord4 == "c": 
        print("Bye")
        exit()
    else: 
        print("Kies a, b of c")
        print(vraag4())

def vraag3(): 
    print("Met welk vervoer ga je naar school?")
    print("a = Bus")
    print("b = Trein")
    print("c = Fiets")
    antwoord3 = input()
    if antwoord3 == "a": 
        print("Dan ben je lang onderweg.")
        print(vraag4())
    elif antwoord3 == "b": 
        print("Dan ben je snel op school.")
        print(vraag4())
    elif antwoord3 == "c":
        print("Lekker willen 'sporten' voor school.")
        print(vraag4())
    else: 
        print("Kies: a, b of c")
        print(vraag3())
        
def vraag2():
    print("Wat ga je eten?")
    print("a = Brood")
    print("b = Yoghurt")
    print("c = Niks")
    antwoord2 = input()
    if antwoord2 == "a": 
        print("Goed zo.")
        time.sleep(0.5)
        print(vraag3())
    elif antwoord2 == "b": 
        print("Lekker met wat fruit.")
        print(vraag3())
    elif antwoord2 == "c": 
        print("verstandig.")
        print(vraag3())
    else: 
        print("Kies: a, b of c")
        print(vraag2())
        
def vraag1():
    print("Ga je opstaan?")
    print("a = Ja")
    print("b = Nee.")
    antwoord1 = input()
    if antwoord1 == "a":
        print("Goed zo nu kom je optijd.\n")
        time.sleep(0.5)
        print(vraag2())
    elif antwoord1 == "b": 
        print("Verstandig...\n")
        print(vraag1())
    else: 
        print("Kies: a of b")
        print(vraag1())
   
print(vraag1())