def scores(filename):
    """Wyświetlenie aktualnej tablicy najlepszych wyników."""
    try:
        with open(filename) as f_obj:
            players = f_obj.readlines()
    except FileNotFoundError:
        msg = "Przepraszamy, ale plik '" + filename + "' nie istnieje."
    else:
        wyniki = []
        for player in players:
            i = 0
            while i < (len(player)-1):
                if player[i] == ' ':
                    i += 1
                    wyniki.append(player[i:len(player)])
                i += 1
        i = 0
        l = len(wyniki)
        while i < l-1:
            j=0
            while j < l-1:
                if wyniki[j] < wyniki[j+1]:
                    pomoc_1 = wyniki[j+1]
                    pomoc_2 = players[j+1]
                    wyniki[j+1] = wyniki[j]
                    players[j+1] = players[j]
                    wyniki[j] = pomoc_1
                    players[j] = pomoc_2
                j += 1
            i += 1           
        if players:
            print("Scoreboard: ")
            i = 1
            l = len(players)
            while i < l:
                print(str(i) + ". " + str(players[i-1]))
                if i == 10:
                    break
                i += 1
#scoreboard('wyniki.txt')
                

