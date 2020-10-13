from random import seed
from random import randint
import time
import sys
import os

def errorNumber():
    print("Błąd. Podaj poprawną liczbę.")

def guessing():
    randomInteger = randint(1, 100)
    while True:
        guess = int(input("Podaj liczbę: "))
        if guess >= 1 and guess <= 100:
            if guess < randomInteger:
                print("za mała liczba")
            elif guess > randomInteger:
                print("za duża liczba")
            elif guess == randomInteger:
                print("brawo, mój przyjacielu\n")
                return False
        else:
            errorNumber()

def dotsAnimation(number, delay): # printing (number) dots every (delay) seconds
    for i in range(number):
        time.sleep(delay) # in seconds
        print(".")
        sys.stdout.flush()

def frame (string):
    tlCorner = chr(9556) # top left corner
    trCorner = chr(9559) # top right corner
    blCorner = chr(9562) # bottom left corner
    brCorner = chr(9565) # bottom right corner
    horPiece = chr(9552) # horizontal piece
    verPiece = chr(9553) # vertical piece
    print(tlCorner + len(string) * horPiece + trCorner)
    print(verPiece + string + verPiece)
    print(blCorner + len(string) * horPiece + brCorner + "\n")

print(20 * chr(9552))
print("1) Rozpocznij grę")
print("2) Pokaż wyniki")
print("3) Zamknij grę")
print(20 * chr(9552))

while True:
    menu = input("\nWybierz w menu: ")
    if menu == "1":
        print("Startujemy")
        dotsAnimation(3, 0.1)
        frame("Zgadywanie")
        timeStart = time.perf_counter()
        if not guessing():
            timeStop = time.perf_counter()
        score = 100000 - round(1000 * timeStop - timeStart)
        print("Wynik: " + str(score) + "\n")
        while True:
            playerName = input("Podaj nazwę gracza: ")
            if ',' in playerName:
                print("Błędna nazwa gracza.")
            else:
                fWyniki = open("wyniki.txt", "a")
                if fWyniki:
                    fWyniki.write(playerName + ", " + str(score) + "\n")
                    fWyniki.close()
                else:
                    print("Błąd otwarcia pliku.")
                break

    elif menu == "2":
        frame("Wyniki")
        #wyniki wczytane z pliku
        break

    elif menu == "3":
        frame("Dziękujemy za grę :)")
        print("Autorzy:\nKamil Giziński\nBartosz Rolnik\nDominik Sigulski")
        dotsAnimation(3, 1)
        break
        os.system("PAUSE")

    else:
        errorNumber()