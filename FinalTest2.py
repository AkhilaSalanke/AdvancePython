from reader import read_col

def Print_captainNames():
    Players = read_col("captains.txt", "Player", str)
    Tied = read_col("captains.txt", "Tied", int)

    headers = ['Player', 'Tied']
    rows = list(zip(Players, Tied))
    TiedPlayers = list()
    for i in range (0,(len(rows))):
        if Tied[i]>0:
            TiedPlayers.append(Players[i])
    return TiedPlayers

if __name__=="__main__":
    Print_captainNames()










