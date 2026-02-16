import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import requests

# ====== Text-to-Speech ======
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Chatbot:", text)
    engine.say(text)
    engine.runAndWait()

# ====== Speech-to-Text (with fallback to text input) ======
def listen():
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            speak("Listening...")
            rec.adjust_for_ambient_noise(source, duration=0.5)
            audio = rec.listen(source, timeout=5, phrase_time_limit=5)
        query = rec.recognize_google(audio)
        print("You:", query)
        return query.lower()
    except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError, OSError):
        # If voice fails, fallback to text input
        query = input("You (type here as fallback): ")
        return query.lower()

# ====== API KEYS ======
OPENWEATHER_API_KEY = "360778482134fd7909b8ae6749967c9b"
NEWS_API_KEY = "695e07af402f4b119f0703e9b19f4683"

# ====== Commands ======
greet_msgs = ["hi", "hello", "hey"]
date_msgs = ["date", "today date", "tell me date"]
time_msgs = ["time", "current time"]
news_msgs = ["news", "headlines"]
weather_msgs = ["weather", "current weather"]

# ====== News ======
def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(url).json()
        articles = response.get("articles", [])
        if not articles:
            speak("No news available")
            return
        speak("Today's top news:")
        for i in range(min(5, len(articles))):
            speak(articles[i]['title'])
    except Exception as e:
        speak("Failed to fetch news.")
        print("News Error:", e)

# ====== Weather ======
def get_location():
    try:
        res = requests.get("http://ip-api.com/json/").json()
        return res.get("city"), res.get("lat"), res.get("lon")
    except:
        return None, None, None

def get_weather():
    city, lat, lon = get_location()
    if city is None:
        speak("Location not detected")
        return
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        condition = data["weather"][0]["description"]
        speak(f"Weather in {city}: {temp}°C, feels like {feels_like}°C, {condition}")
    except Exception as e:
        speak("Failed to fetch weather information.")
        print("Weather Error:", e)

# ====== Main loop ======
speak("Smart voice chatbot started")
running = True

while running:
    user_msg = listen()
    if user_msg == "":
        continue  # skip if nothing heard

    # ===== Commands =====
    if user_msg in greet_msgs:
        speak("Hi! How can I help?")

    elif user_msg in date_msgs:
        speak(f"Today's date is {datetime.now().date()}")

    elif user_msg in time_msgs:
        speak(f"Current time is {datetime.now().strftime('%I:%M:%S %p')}")

    elif "open" in user_msg:
        site = user_msg.split()[-1]
        speak(f"Opening {site}")
        webbrowser.open(f"https://www.{site}.com")

    elif any(word in user_msg for word in news_msgs):
        get_news()

    elif any(word in user_msg for word in weather_msgs):
        get_weather()

    elif "calculate" in user_msg:
        try:
            exp = user_msg.replace("calculate", "")
            result = eval(exp)
            speak(f"Result is {result}")
        except:
            speak("Invalid calculation")

    elif user_msg in ["bye", "exit", "quit"]:
        speak("Goodbye!")
        running = False

    else:
        speak("Searching on Google...")
        webbrowser.open("https://www.google.com/search?q=" + user_msg)
