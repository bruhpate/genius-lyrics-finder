from lyricsgenius import Genius
import re
yourToken = "*replace with your token*"
genius = Genius("yourtoken")
def ask():
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