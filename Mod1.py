from random import seed
from random import randint
import time
import sys
import os

def errorNumber():
    print("Błąd. Podaj poprawną liczbę.")

def guessing():
    timeStart = time.perf_counter()
    randomInteger = randint(1, 100)
    number = 1
    while True:
        try:
            guess = int(input(str(number) + ". Podaj liczbę od 1 do 100: "))
            
        except ValueError:
            errorNumber()
        else:
            if guess >= 1 and guess <= 100:
                if guess < randomInteger:
                    print("za mała liczba")
                elif guess > randomInteger:
                    print("za duża liczba")
                elif guess == randomInteger:
                    print("brawo, mój przyjacielu\n")
                    timeStop = time.perf_counter()
                    timeDifference = round(1000 * (timeStop - timeStart))
                    return timeDifference
                number += 1
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
    print(blCorner + len(string) * horPiece + brCorner)

print(chr(9556) + 20 * chr(9552) + chr(9559))
print(chr(9553) + "1) Rozpocznij grę" + (20 - len("1) Rozpocznij grę")) * ' ' + chr(9553))
print(chr(9553) + "2) Pokaż wyniki" + (20 - len("2) Pokaż wyniki")) * ' ' + chr(9553))
print(chr(9553) + "3) Zamknij grę" + (20 - len("3) Zamknij grę")) * ' ' + chr(9553))
print(chr(9562) + 20 * chr(9552) + chr(9565))

while True:
    menu = input("\nWybierz w menu: ")
    if menu == "1":
        frame("Zgadywanie")
        dotsAnimation(3, 0.1)
        print("\nStartujemy")
        temp = guessing()
        if temp <= 1000000:
            score = 1000000 - temp
        else:
            score = 1
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
        dotsAnimation(3, 0.2)
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
