import webbrowser
from textblob import TextBlob
import random

playlists_choice = {
    "positive": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
        "https://www.youtube.com/watch?v=SW_iujvUAzQ"  
    ],
    "negative": [
        "https://www.youtube.com/watch?v=PcvngjNBGHI"  
    ],
    "neutral": [
        "https://www.youtube.com/watch?v=F4tHL8reNCs"  
    ]
}

phrase = input("How are you feeling today? ")


blob = TextBlob(phrase)
score = blob.sentiment.polarity
mood = ""


if score > 0:
    mood = "positive"
    print(f"Great!I will play happy music 🎵")

elif score < 0:
    mood = "negative"
    print(f"Oh... sorry about that.I will play you something to cheer you up ❤️")

else:
    mood = "neutral"
    print("Neutral mood detected. Let's play something anyways ☕")


song_url = random.choice(playlists_choice[mood])
print(f"Opening YouTube: {song_url}")
webbrowser.open(song_url)
