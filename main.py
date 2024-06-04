# Herní automat v Pythonu
from os import system

isRunning = True
penize = 100
sazka = 10
volba = 0

def vypisZustatek():
    global penize
    print(f"Váš zůstatek je {penize} peněz!")
    print(f"Vaše sázka je {sazka} peněz!")

def upravitSazku():
    global sazka
    withoutProblem = True
    novaSazka = input("Zadejte novou sázku: ")

    if not novaSazka.isdigit():
        print("Zadejte číslo!")
        withoutProblem = False

    else:
        if int(novaSazka) <= 0:
            print("Sázka musí být více než 0!")
            withoutProblem = False

        if int(novaSazka) > 1000:
            print("Maximální možná sázka je 1000!")
            withoutProblem = False

    if withoutProblem:
        sazka = novaSazka
        print(f"Sázka nastavena na {sazka} peněz!")

    

while isRunning:
    print("#############################")
    print("     Hlavní menu")
    print("(1) Zobrazit zůstatek")
    print("(2) Zatočit")
    print("(3) Upravit sázku")
    print("(4) Konec")
    print("#############################")

    volba = input("Vyberte akci: ")

    system("cls")

    if volba == "1":
        vypisZustatek()
        
    elif volba == "2":
        pass

    elif volba == "3":
        upravitSazku()

    elif volba == "4":
        isRunning = False
