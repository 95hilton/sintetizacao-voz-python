import pyttsx3
import webbrowser
import speech_recognition as sr

#função responsável por dizer algum texto ao usuário
def say_something(text):
    en = pyttsx3.init()
    en.say(text)
    en.setProperty('voice',b'brazil')
    en.setProperty('rate',140)
    en.setProperty('volume',1)
    en.runAndWait()

#função responsável por capturar resposta do usuário
def recognizer():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recon.listen(source)
        response = recon.recognize_google(audio,language='pt')
        print(response)
        return response


say_something("Olá! O que você deseja?")
response = recognizer()

#valida resposta do usuário
if "Google" in response:
    say_something("Ok, estou abrindo o Google para você.")
    webbrowser.open('www.google.com.br')

elif "notícias" in response:
    say_something("Ok, estou abrindo as notícias para você.")
    webbrowser.open('www.em.com.br')

else:
     say_something("Não entendi sua resposta. Vamos tentar novamente mais tarde")

