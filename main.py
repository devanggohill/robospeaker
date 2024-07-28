import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
#text = "Python text-to-speech test. using win32com.client"
#speak.Speak(text)

if __name__ == '__main__':
    while True:
        x  = input("Enter what you want me to speak ")
        if x == "q":
            speak.Speak("bye bye friend ")
            break

        speak.Speak(x)