
import speech_recognition as sr
import pyaudio
recog=sr.Recognizer()

print("i'm Listning you...")

with sr.Microphone() as m:
    audio=recog.listen(m)
    listen=recognize(audio)


listen1=listen.lower()

if listen1 in "hello":
    print("Hi! Welcome to python how may I help you")

elif listen1 in "date":
    from datetime import date
    print(listen)
    print(date.today())

elif listen1 in "time":
    from time import strftime
    print(listen)
    print(strftime("%I : %M"))

elif listen1 in "date" and "time":
    print(listen)
    print(date.today())
    print(strftime("%I : %M"))

#google search

else:
    from googlesearch import search
    for url in search(listen1,tld=com,lang=en,stary=0,stop=10,pause=2):
        print(listen)    
        print(url)    
