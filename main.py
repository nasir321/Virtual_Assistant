# install few libraries using pip command,
# import few libraries
import speech_recognition as sr  # pip install speech_recognition
import pyttsx3  # pip install pyttsx3
import pywhatkit  # pip install pywhatkit
import datetime  # pip install datetime
import webbrowser  # pip install webbrowser
import wikipedia  # pip install wikipedia

# listening and recognizing voice
listener = sr.Recognizer()
engine = pyttsx3.init()

# change voice property male/femail voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voice id [1] for femail, [0] for male voice
print("Hi Dear, what can i do for you.")  # print on screen
engine.say('Hi Dear, what can i do for you.')  # system say
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:  # get input via microphone
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('alexa', '')
            print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    # print(command)
    if 'play' in command:
        song = command.replace('paly', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('Current time is ' + time)

    elif 'google' in command:
        webbrowser.open('https://google.com/?#q' + command)

    elif 'youtube' in command:
        webbrowser.open('https://youtube.com/?#q' + command)

    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    else:
        talk('Please say the command again. Thanks')


while True:
    run_alexa()