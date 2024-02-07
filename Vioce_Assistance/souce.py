import pyttsx3
import speech_recognition as sr

def sptext():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening....")
        audio = recognizer.listen(source)

        try:
            print("Recognizing....!")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
        except sr.UnknownValueError:
            print("Could not understand audio")

sptext()



