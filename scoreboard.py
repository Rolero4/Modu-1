def scores(filename):
    try:
        with open(filename) as f_obj:
            players = f_obj.readlines()
    except FileNotFoundError:
        print("Przepraszamy, ale plik '" + filename + "' nie istnieje.")
    else:
        results = []
        for player in players:
            i = 0
            while i < (len(player)-1):
                if player[i] == ' ':
                    i += 1
                    results.append(player[i:len(player)])
                i += 1
        i = 0
        l = len(results)
        while i < l-1:
            j=0
            while j < l-1:
                if results[j] < results[j+1]:
                    tempResults = results[j+1]
                    tempPlayers = players[j+1]
                    results[j+1] = results[j]
                    players[j+1] = players[j]
                    results[j] = tempResults
                    players[j] = tempPlayers
                j += 1
            i += 1           
        if players:
            print("Scoreboard:\n")
            i = 1
            l = len(players)
            while i < l:
                print(str(i) + ". " + str(players[i-1]))
                if i == 10:
                    break
                i += 1
