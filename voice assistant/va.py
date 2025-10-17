import pyttsx3
import webbrowser
import datetime
engine = pyttsx3.init()
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def show_instructions():
    print("\nAvailable Instructions:")
    print("- what can you do for me")
    print("- current time")
    print("- open google")
    print("- open youtube")
    print("- open gmail")
    print("- shutdown")
    print("- instructions (to show this list again)\n")

def process_instruction(instruction):
    instruction = instruction.lower()

    if 'what can you do for me' in instruction:
        speak('I tell time, play song and help you go with wikipedia')

    elif 'current time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)

    elif 'open google' in instruction:
        speak('Opening Google')
        webbrowser.open('https://google.com')

    elif 'open youtube' in instruction:
        speak('Opening YouTube')
        webbrowser.open('https://youtube.com')

    elif 'open gmail' in instruction:
        speak('Opening Gmail')
        webbrowser.open('https://gmail.com')

    elif 'shutdown' in instruction:
        speak('I am shutting down')
        exit()  
        return False
    else:
        speak('I did not understand, can you repeat again')
    return True
def start():
    show_instructions()
    while True:
        instruction = input("give your instructions: ")  
        if not process_instruction(instruction):
            break
start()
