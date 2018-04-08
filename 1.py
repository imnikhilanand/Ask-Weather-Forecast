import re 
import nltk
#nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from urllib.request import urlopen
import json

string2 = "what is the temperature of Mumbai"


def tell_weather(string):
    stop_words = set(stopwords.words('english')) 
    review = re.sub('[^a-zA-Z]',' ',string) 
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    new_arr = []
    new_arr2 = []
    new_arr3 = []
    """for word in review:
        array_new.append(ps.stem(word))"""
        #print(array_new)

    """for r in array_new:
        if not r in stop_words:
            new_arr.append(r)"""

    for r in review:
        if not r in stop_words:
            new_arr.append(r)
        
        #print(new_arr)        
       
        #print(stop_words)
        
        temp_words = set()  
        temp_words.add("temperature")
        temp_words.add("humidity")
        temp_words.add("pressure")
        temp_words.add("maximum")   
        temp_words.add("minimum")
        #print(temp_words)
        

    for m in new_arr:
        if not m in temp_words:
            new_arr2.append(m)        
        else:
            new_arr3.append(m)    

        #print(new_arr2)
        #print(new_arr3)

        #print(stop_words)
        #type(stop_words)
        #print(temp_words)

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
    
    # Get the dataset
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=c140dd2e860dc97628ab3a2397aa6183&q='+new_arr2[0]
    response = urlopen(url)

    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    # prints the string with 'source_name' key
    
    print(json_obj['main'][new_arr4[0]]-273.15)
    return;


tell_weather(string = string2)


    