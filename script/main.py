from lyricsgenius import Genius
import re

#IMPORTANT, INSTALL GENIUS MODULE FOR USE IT --> pip install lyricsgenius

token = "UEYB1W3K8BHWH3LM6eg2pn5H_CYzuV0vmInpzUDSngUJWm_H6s-k3-nFoWKn2EnI"
genius = Genius(token)
def ask():
    print("Search a song: ", end="")
    try:
        song = genius.lyrics(genius.search_song(input()).id, None, False)
        x = re.sub("Embed$", "", song)
        for i in range(0, 5):
            x = re.sub("[0-9]$", "", x)
        print(x)
    except:
        None
ask()
