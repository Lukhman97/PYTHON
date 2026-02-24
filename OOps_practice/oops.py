import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os
import sys
import time
import requests
import pyjokes
import smtplib
from email.mime.text import MIMEText
import platform
import psutil


def init_tts(rate=160, volume=1.0, voice_index=None):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    if voice_index is not None and 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    return engine

engine = init_tts()

def speak(text):
    if not text:
        return
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()

def take_command(timeout=6, phrase_time_limit=8):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            print("No speech detected (timeout).")
            return None
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-IN')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return None


def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")
    print("Time ->", now)

def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greet = "Good morning"
    elif 12 <= hour < 17:
        greet = "Good afternoon"
    elif 17 <= hour < 22:
        greet = "Good evening"
    else:
        greet = "Hello"
    speak(f"{greet}. I am your assistant. How can I help you today?")
    print(greet)

def search_wikipedia(query, sentences=2):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=sentences)
        print("Wikipedia result:\n", result)
        speak(result)
    except Exception as e:
        print("Wikipedia error:", e)
        speak("Sorry, I couldn't find that on Wikipedia.")

def open_website(site):
    if not site.startswith(("http://", "https://")):
        if "." not in site:
            site = "http://www." + site + ".com"
        else:
            site = "http://" + site
    webbrowser.open(site)
    speak(f"Opening {site}")

def web_search(query):
    url = "https://www.google.com/search?q=" + webbrowser.quote(query)
    webbrowser.open(url)
    speak("Here are the search results for " + query)

def play_on_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + webbrowser.quote(query)
    webbrowser.open(url)
    speak("Playing results for " + query + " on YouTube")

def write_note(text, filename="notes.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {text}\n")
    speak("Note saved.")
    print(f"Saved note to {filename}")


def get_weather(city="Hyderabad"):
    api_key = "YOUR_API_KEY"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response["cod"] != 200:
            speak("I couldn't get the weather for that city.")
            return
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degree Celsius with {desc}.")
        print(f"Weather -> {temp}°C, {desc}")
    except Exception as e:
        speak("Error fetching weather.")
        print(e)

def calculator():
    speak("Tell me the math expression, for example: 2 plus 2")
    expr = take_command()
    if expr:
        expr = expr.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")
        try:
            result = eval(expr)
            speak(f"The result is {result}")
            print(f"Calculator -> {result}")
        except:
            speak("Sorry, I could not calculate that.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print("Joke:", joke)

def open_app(app_name):
    app_name = app_name.lower()
    if "notepad" in app_name:
        os.system("notepad")
    elif "calculator" in app_name:
        os.system("calc")
    elif "chrome" in app_name:
        os.system("start chrome")
    else:
        speak(f"I don't know how to open {app_name}")

def set_reminder():
    speak("What should I remind you about?")
    task = take_command()
    if not task:
        speak("No task received.")
        return
    speak("In how many minutes should I remind you?")
    minutes = take_command()
    try:
        minutes = int(minutes)
        speak(f"Reminder set for {minutes} minutes from now.")
        time.sleep(minutes * 60)
        speak(f"Reminder: {task}")
    except:
        speak("Invalid time entered.")




def send_email():
    speak("Who is the recipient?")
    recipient = take_command()
    speak("What is the message?")
    message = take_command(phrase_time_limit=30)
    
    if recipient and message:
        sender_email = "your_email@gmail.com"
        sender_pass = "your_password"  
        try:
            msg = MIMEText(message)
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = "Message from Assistant"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_pass)
            server.send_message(msg)
            server.quit()
            speak(f"Email sent to {recipient}")
            print("Email sent successfully!")
        except Exception as e:
            speak("Failed to send email.")
            print(e)


def system_info():
    uname = platform.uname()
    speak(f"System: {uname.system}, Node Name: {uname.node}")
    speak(f"Processor: {uname.processor}")
    ram = psutil.virtual_memory().total / (1024**3)
    speak(f"Total RAM: {ram:.2f} GB")
    print(f"System Info -> {uname}, RAM -> {ram:.2f} GB")

def get_news():
    api_key = "YOUR_NEWSAPI_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        response = requests.get(url).json()
        articles = response["articles"][:5]
        for i, article in enumerate(articles, 1):
            speak(f"Headline {i}: {article['title']}")
            print(f"{i}. {article['title']}")
    except Exception as e:
        speak("Couldn't fetch news.")
        print(e)

def random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url).json()
        fact = response["text"]
        speak(f"Here's a random fact: {fact}")
        print("Fact ->", fact)
    except Exception as e:
        speak("Couldn't fetch a fact.")
        print(e)


def countdown_timer():
    speak("For how many seconds should I set the timer?")
    secs = take_command()
    try:
        secs = int(secs)
        speak(f"Timer set for {secs} seconds.")
        time.sleep(secs)
        speak("Time's up!")
    except:
        speak("Invalid number of seconds.")


def assistant_loop():
    greet_user()
    while True:
        speak("Listening for a command. Say 'help' for options.")
        query = take_command()
        if query is None:
            speak("I didn't catch that. Please say that again.")
            continue

        if any(kw in query for kw in ("exit", "quit", "stop", "goodbye", "bye")):
            speak("Goodbye. Have a nice day!")
            print("Exiting assistant.")
            break


        if "help" in query:
            help_text = (
                "You can say: time, weather, open website, search wiki about something, "
                "search the web, play on youtube, take a note, joke, calculator, open app, reminder, "
                "email, system info, news, random fact, timer, or exit."
            )
            speak(help_text)
            print(help_text)
            continue

      
        if "time" in query:
            tell_time()
            continue


        if "weather" in query:
            speak("Which city?")
            city = take_command()
            if city:
                get_weather(city)
            continue

  
        if query.startswith("wikipedia") or "wikipedia" in query:
            q = query.replace("wikipedia", "").strip()
            if not q:
                speak("What should I search on Wikipedia?")
                q = take_command()
                if not q:
                    continue
            search_wikipedia(q)
            continue

        if query.startswith("open ") or query.startswith("go to "):
            parts = query.split()
            if "open" in parts:
                idx = parts.index("open")
                site = " ".join(parts[idx+1:])
            elif "go" in parts and "to" in parts:
                idx = parts.index("to")
                site = " ".join(parts[idx+1:])
            else:
                site = ""
            if site:
                open_website(site.replace(" ", ""))
            else:
                speak("Which site should I open?")
            continue


        if "play" in query and "youtube" not in query:
            q = query.replace("play", "").strip()
            if q:
                play_on_youtube(q)
            continue
        if "youtube" in query:
            q = query.replace("on youtube", "").replace("youtube", "").strip()
            if not q:
                speak("What should I search on YouTube?")
                q = take_command()
                if not q:
                    continue
            play_on_youtube(q)
            continue


        if query.startswith("search ") or query.startswith("google ") or "search for" in query:
            q = query.replace("search", "").replace("google", "").replace("for", "").strip()
            if not q:
                speak("What should I search for?")
                q = take_command()
                if not q:
                    continue
            web_search(q)
            continue


        if "note" in query or "remember" in query or "write this" in query:
            speak("What should I write down?")
            note_text = take_command(phrase_time_limit=15)
            if note_text:
                write_note(note_text)
            continue


        if "joke" in query or "funny" in query:
            tell_joke()
            continue


        if "calculate" in query or "calculator" in query:
            calculator()
            continue


        if "open app" in query or "launch" in query:
            speak("Which application should I open?")
            app_name = take_command()
            if app_name:
                open_app(app_name)
            continue


        if "remind me" in query or "reminder" in query:
            set_reminder()
            continue

        if "email" in query:
            send_email()
            continue

  
        if "system info" in query or "my computer" in query:
            system_info()
            continue

        if "news" in query:
            get_news()
            continue


        if "fact" in query:
            random_fact()
            continue


        if "timer" in query or "countdown" in query:
            countdown_timer()
            continue


        speak("I am not sure how to help with that. Should I search the web for it?")
        ans = take_command()
        if ans and any(w in ans for w in ("yes", "yeah", "sure", "okay", "yep")):
            web_search(query)
        else:
            speak("Okay, let me know another command.")


if __name__ == "__main__":
    try:
        assistant_loop()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        speak("Shutting down. Bye.")
        sys.exit(0)
