#library for json 

from urllib2 import urlopen
import json
import pyttsx


#library for nltk
import re 
import nltk
#nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords



#library for speech recognition
import speech_recognition as sr 
r = sr.Recognizer()
import sys

#function t take voice input
def bol_bhai():
	with sr.Microphone() as source:
		#print('Say Something')
		audio = r.listen(source)

	try:
		abc = r.recognize_google(audio)

	except:
		pass	
	return abc


new_arr = []
new_arr2 = []
new_arr3 = []
new_arr4 = []    

def tell_weather(string):
    stop_words = set(stopwords.words('english')) 
    review = re.sub('[^a-zA-Z]',' ',string) 
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    
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
    	
    for x in new_arr3:
        if x == "maximum":
            new_arr4.append("temp_max")
        if x == "minimum":
            new_arr4.append("temp_min")
        if x == "temperature":
            new_arr4.append("temp") 
        if x == "pressure":
            new_arr4.append("pressure")
        if x == "humidity":    
            new_arr4.append("humidity")


#speck engine to give speech output

speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init nsss for mac
speech_engine.setProperty('rate', 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()



#speak("Ask weather forecast")
text=bol_bhai()
#tell_weather("What is Patna maximum temperature")
tell_weather(text)



# Weather api to predict weather
url = 'http://api.openweathermap.org/data/2.5/weather?appid=c140dd2e860dc97628ab3a2397aa6183&q='+new_arr2[0]
response = urlopen(url)
string = response.read().decode('utf-8')
json_obj = json.loads(string)
resu=json_obj['main'][new_arr4[0]]-273.15
    

p = str(resu)
q = str(new_arr2[0])
r = str(new_arr4[0])

#print(r)
#speak(r)


if r == "temp_max":
	speak(q+" maximum temperature is "+ p +" degree celcius")
elif r == "temp_min":
	speak(q+" minimum temperature is "+ p +" degree celcius")
elif r == "humidity":
	speak(q+" humidity is "+ p)
elif r == "temp":
	speak(q+" temperature is "+ p +" degree celcius")
elif r == "pressure":
	speak(q+" pressure is "+ p +" newton meter")

sys.exit()


