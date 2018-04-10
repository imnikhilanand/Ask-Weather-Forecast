import speech_recongnition as sr
import re 
import nltk
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from urllib.request import urlopen
import json
import pyttsx

speech_engine = pyttsx.init('espeak') 
speech_engine.setProperty('rate', 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()


def tell_weather(string):
    stop_words = set(stopwords.words('english')) 
    review = re.sub('[^a-zA-Z]',' ',string) 
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    new_arr = []
    new_arr2 = []
    new_arr3 = []
    

    for r in review:
        if not r in stop_words:
            new_arr.append(r)
        
        temp_words = set()  
        temp_words.add("temperature")
        temp_words.add("humidity")
        temp_words.add("pressure")
        temp_words.add("maximum")   
        temp_words.add("minimum")
        

    for m in new_arr:
        if not m in temp_words:
            new_arr2.append(m)        
        else:
            new_arr3.append(m)    

    new_arr4 = []

    for x in new_arr3:
        if x == "temperature":
            new_arr4.append("temp") 
        if x == "maximum":
            new_arr4.append("temp_max")
        if x == "minimum":
            new_arr4.append("temp_min")
        if x == "pressure":
            new_arr4.append("pressure")
        if x == "humidity":    
            new_arr4.append("humidity")
    
    # Weather api to predict weather
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=c140dd2e860dc97628ab3a2397aa6183&q='+new_arr2[0]
    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    print(json_obj['main'][new_arr4[0]]-273.15)
    return;



r = sr.Recognizer();
with sr.Microphone() as source:
    speak("Hey I am here to tell you the weeather forecast, ask me")
    audio = r.listen(source)
try:
    string = r.recognize_google(audio)
    tell_weather(string = string2)
except: 
    pass


    
    
