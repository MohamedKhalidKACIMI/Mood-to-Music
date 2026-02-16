#Mood-to-Music Bot

A Python project that uses **Natural Language Processing (NLP)** to detect your current mood and automatically plays the perfect music track on YouTube.

##Description

This project was built to explore the basics of **Sentiment Analysis** applied to a daily task: choosing music.

The user describes their day or feelings in a single sentence, and the algorithm:
1.  **Analyzes** the text polarity (Positive / Negative / Neutral) using `TextBlob`.
2.  **Selects** a curated playlist based on the calculated score.
3.  **Automates** the web browser to play a randomly selected song.

##Technologies Used

* **Python 3**
* **TextBlob** (NLP library for sentiment analysis)
* **Webbrowser & Random** (Standard Python automation libraries)

##Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/MohamedKhalidKACIMI/Mood-to-Music.git]
    ```

2.  **Install dependencies**
    ```bash
    pip install textblob
    ```

3.  **Run the script**
    ```bash
    python mood_music.py
    ```

##How it Works

The core logic relies on `TextBlob`'s polarity score, which ranges from -1 to 1.

```python
blob = TextBlob(user_input)
score = blob.sentiment.polarity

if score > 0:
    print("Mood: Positive ☀️")
    # Plays happy music
elif score < 0:
    print("Mood: Negative 🌧️")
    # Plays comforting music
