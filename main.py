# Herní automat v Pythonu
from os import system
from random import randint
from time import sleep

def vypisZustatek():
    global penize
    print(f"Váš zůstatek je {penize} peněz!")
    print(f"Vaše sázka je {sazka} peněz!")

def upravitSazku():
    global sazka
    withoutProblem = True
    novaSazka = input("Zadejte novou sázku: ")
    system("cls")

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

        if int(novaSazka) > penize:
            print(f"Nedostatek kreditu! Stav vašeho kreditu je {penize} peněz!")
            withoutProblem = False

    if withoutProblem:
        sazka = int(novaSazka)
        print(f"Sázka nastavena na {sazka} peněz!")

def spin():
    znaky: list[str] = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    kombinace: list[str] = ["  ", "  ", "  "]
    global penize

    if penize >= sazka:
        penize -= sazka

        # Zatočení
        for i in range(3):
            # Animace točení
            for j in range(10):
                kombinace[i] = znaky[randint(0, 4)]
                system("cls")
                print("----------")
                print(f"|{kombinace[0]}|{kombinace[1]}|{kombinace[2]}|")
                print("----------")
                sleep(0.05)

            kombinace[i] = znaky[randint(0, 4)]
            system("cls")
            print("----------")
            print(f"|{kombinace[0]}|{kombinace[1]}|{kombinace[2]}|")
            print("----------")
            sleep(0.5)
        
        # Vyhodnocení výhry nebo prohry
        if kombinace[0] == kombinace[1] == kombinace[2]:
            print(f"Výhra! Vyhráli jste {4 * sazka}!")
            penize += 4 * sazka
            return

        if kombinace[0] == kombinace[1] or kombinace[1] == kombinace[2]:
            print(f"Částečná výhra! Vyhráli jste {2 * sazka}!")
            penize += 2 * sazka
            return
            
        else:
            print("Prohra!")

    else:
        print("Nedostatek kreditu!")


def main():
    isRunning = True
    global penize
    penize = 100
    global sazka
    sazka = 10
    volba = 0
    volby = ["1", "2", "3"]

    while isRunning:
        if penize == 0:
            system("cls")
            print("Váš kredit je 0, konec hry!")
            break

        vypisZustatek()
        print("#############################")
        print("     Hlavní menu")
        print("(1) Zatočit")
        print("(2) Upravit sázku")
        print("(3) Konec")
        print("#############################")

        volba = input("Vyberte akci: ")

        system("cls")

        if not volba.isdigit():
            print("Zadejte číslo!")
            continue

        if volba not in volby:
            print("Vyberte číslo z menu!")
            continue
            
        elif volba == "1":
            spin()

        elif volba == "2":
            upravitSazku()

        elif volba == "3":
            isRunning = False

if __name__ == "__main__":
    main()
