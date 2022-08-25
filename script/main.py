from lyricsgenius import Genius
import re

#IMPORTANT, INSTALL GENIUS MODULE FOR USE IT --> pip install lyricsgenius

token = "UEYB1W3K8BHWH3LM6eg2pn5H_CYzuV0vmInpzUDSngUJWm_H6s-k3-nFoWKn2EnI"
genius = Genius(token)
def ask():
    print("Search the song: ", end="")
    try:
        song = genius.lyrics(genius.search_song(input()).id, None, False)
        x = re.sub("Embed$", "", song)
        x = re.sub("[0-9]Embed$", "", x)
        x = re.sub("[0-9]$", "", x)
        print(x)
    except:
        None
ask()
