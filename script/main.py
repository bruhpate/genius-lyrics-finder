from lyricsgenius import Genius
import re


#replace the value of this variable with your genius token, or generate one --> https://genius.com/api-clients
yourToken = "*replace with your token*"
genius = Genius(yourToken)
def ask():
    print("Search the song: ")
    try:
        song = genius.lyrics(genius.search_song(input()).id, None, False)
        x = re.sub("Embed$", "", song)
        x = re.sub("[0-9]Embed$", "", x)
        x = re.sub("[0-9]$", "", x)
        print("\n")
        print(x)
    except:
        None
ask()