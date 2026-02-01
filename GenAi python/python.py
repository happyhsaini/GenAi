from datetime import datetime
import webbrowser
import requests

# Corpus
greet_msgs = ["hi", "hello", "hey", "hi there", "hello there"]
date_msgs = ["date", "tell me date", "today's date"]
time_msgs = ["time", "tell me time", "current time"]
news_msgs = ["tell me new", "news", "headlines"]

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    for i in range(len(articles)):
        print(articles[i]['title'])

chat = True
while chat:
    user_msg = input("Enter your message : ").lower()

    # if user_msg == "hi" or user_msg == "hello" or user_msg == "hey":
    if user_msg in greet_msgs:
        print("Hello User. How may I help you ?")
    elif user_msg in date_msgs:
        print(f"Today's date is : {datetime.now().date()}")
    elif user_msg in time_msgs:
        current_time = datetime.now().time()
        print("Time is:",current_time.strftime("%I:%M:%S %p"))
    elif "open" in user_msg:
        website_name = user_msg.split()[-1]
        webbrowser.open(f"https://www.{website_name}.com")
    elif user_msg in news_msgs:
        get_news()
    elif "calculate" in user_msg:
        expression = user_msg.split()[-1]
        result = eval(expression)
        print("Result is :",result)
    elif user_msg == "bye":
        chat = False
    else:
        print("I cannot understand")