import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import os
import smtplib


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon Sir!")
    else:
        speak("Good Evening Sir!")


speak("Hello Sir, I am Jarvis, your personal assistant. How can I help you?")


# Creating Email Connection Using SMTP
def sendEmail(to, content):
    try:
        # Read the password from a file
        with open ("password.txt","r") as file:
            password = file.read().strip()

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        # Log in to the sender's email account
        server.login("gill3519@gmail.com", password)

        # Send the email
        server.sendmail("gill3519@gmail.com", to, content)
        server.close()

        print("The Email has been sent successfully.")
        speak("The Email has been sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("The email could not be sent.")


# creating Artificial Intelligence Speech Recognition Model
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    try:
        print("Rcognizing.....")
        query = r.recognize_google(audio)
        print(f"User said....{query}")
    except:
        print("could you try that again, please?")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Simple conversational responses
        if "hello" in query or "hi" in query:
            speak("Hello Sir! How can I help you?")
        elif "how are you" in query:
            speak(
                "I am just a program, but I am functioning as expected. How can I assist you?"
            )
        elif "who are you" in query:
            speak(
                "I am Jarvis, your personal assistant. I am here to help you with your tasks."
            )
        elif "what can you do" in query:
            speak(
                "I can perform various tasks like opening websites, playing music, telling the time, sending emails, and fetching information from the internet."
            )
        elif "thank you" in query or "thanks" in query:
            speak(
                "You're welcome! Let me know if there's anything else I can do for you."
            )
        elif "what's your name" in query:
            speak("My name is Jarvis. I am your personal assistant.")
        elif "stop" in query or "exit" in query or "quit" in query:
            speak("Goodbye, Sir! Have a great day!")
            break

        # Detect general queries for Wikipedia
        if "tell me about" in query or "what is" in query or "who is" in query:
            try:
                # Extract the topic from the query
                if "tell me about" in query:
                    query = query.replace("tell me about", "").strip()
                elif "what is" in query:
                    query = query.replace("what is", "").strip()
                elif "who is" in query:
                    query = query.replace("who is", "").strip()

                # Open the Wikipedia page for the query
                url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
                webbrowser.open(url)
                speak(f"Here is the Wikipedia page for {query}")
            except Exception as e:
                print("Cannot find a search related to Wikipedia")
                speak("Cannot find a search related to Wikipedia")

        # Other commands
        elif "open stack overflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com/")
        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com/")
        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com/")
        elif "open twitter" in query:
            speak("Opening Twitter")
            webbrowser.open("https://twitter.com/")
        elif "open linkedin" in query:
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com/")
        elif "open whatsapp" in query:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com/")
        elif "open gmail" in query:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com/")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        elif "open amazon" in query:
            speak("Opening Amazon")
            webbrowser.open("https://www.amazon.in/")
        elif "close my browser" in query:
            os.system("taskkill /f /im msedge.exe")
            speak("Closing Browser")

        # Playing Music
        elif "play music" in query:
            music_path = "C:\\Users\\deep\\Music"
            list = os.listdir(music_path)
            os.startfile(os.path.join(music_path, list[0]))
            speak("Playing Music")
        elif "close music" in query or "stop music" in query:
            os.system("taskkill /f /im music.exe")
            speak("Closing Music")
        # Date and Time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(f"The Current time is {time}")
            speak(time)
        elif "date" in query:
            date = datetime.datetime.now().date()
            print(f"The Current date is {date}")
            speak(date)
        # Sending Email
        elif "send email" in query:
            try:
                speak("What do you want to say?")
                content = takeCommand().lower()
                to = "deep02102004@gmail.com"
                sendEmail(to, content)
                print("The Email has been sent")
                speak("The Email has been sent")
            except:
                print("The Email has not been sent")
                speak("The Email has not been sent")
        elif "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
        elif "open cmd" in query:
            path = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(path)
        