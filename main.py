import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer() 
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            kuttan_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            kuttan_speak('Asshole say clearly')
        except sr.RequestError:
            kuttan_speak('Im down , Mamanodu Onnum Thonalle')
    return voice_data

def kuttan_speak(audio_string):
    tts = gTTS(text = audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file='audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string + "\n\n")
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        kuttan_speak('You can call me Kuttan')
    if 'kutta time' in voice_data:
        kuttan_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        kuttan_speak('Here you go ' + search)
    if 'find location' in voice_data:
        location = record_audio('Where do you want to look for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        kuttan_speak('Here is the location of ' +location)
    if 'get lost' in voice_data:
        kuttan_speak('Ok bye')
        exit()
    if 'play video' in voice_data:
        video = record_audio('What do you want to play?')
        url = 'https://www.youtube.com/results?search_query=' + video
        webbrowser.get().open(url)
        kuttan_speak('Here is the video of ' + video+'. Enjoy')



time.sleep(1)
print("------------------------------COMMANDS---------------------------------")
print("")
print("                   Try like what is your name")
print("                   Kutta Time -     Gives you time")
print("                   Search     -    Asks you what to search")
print("                   find location- Asks you the location to look for")
print("                   play video-    Asks you the video to play")
print("                   Get lost   -    Exits")
kuttan_speak('How can I help You Kutta ?')
while 1:
     voice_data = record_audio()
     print("\t\t\t\t\t\t" + voice_data + "\n\n")
     respond(voice_data)
     kuttan_speak('Anything else kutta')
