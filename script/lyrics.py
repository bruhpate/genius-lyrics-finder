from lyricsgenius import Genius
import re
import sys

#IMPORTANT, INSTALL GENIUS MODULE FOR USE IT --> pip install lyricsgenius

token = "UEYB1W3K8BHWH3LM6eg2pn5H_CYzuV0vmInpzUDSngUJWm_H6s-k3-nFoWKn2EnI"
genius = Genius(token)
def ask():
    try:
        song = genius.lyrics(genius.search_song(sys.argv[1]).id, None, False)
        x = re.sub("Embed$", "", song)
        x = removeN(x)
        print(x)
    except:
        None

def removeN(x):
    if bool(re.search("[0-9]$", x)) == True:
        x = re.sub("[0-9]$", "", x)
        x = removeN(x)
    return x    


def main():
    try:
        y = sys.argv[1]
        ask()
    except:
        print("Usage: lyrics [\"title and artist\"]")
        exit


if __name__ == "__main__":
    main()          

