import pyttsx3

text_speech = pyttsx3.init()
text= input("Enter your text to speek: ")
text_speech.say(text)
text_speech.runAndWait()
