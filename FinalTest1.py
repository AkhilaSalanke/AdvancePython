from reader import read_col

def Print_NumofCaptains(Tied_matches):
    Tied_matches_list = list()
    for i in range (0,(len(Tied_matches))):
        if Tied_matches[i]>0:
            val = int(Tied_matches[i])
            Tied_matches_list.append(val)
    return len(Tied_matches_list)

if __name__=="__main__":
    Tied_matches = read_col("captains.txt", "Tied", int)
    Print_NumofCaptains(Tied_matches)
    print(Print_NumofCaptains(Tied_matches), "Captains had atleast one Tied match")









