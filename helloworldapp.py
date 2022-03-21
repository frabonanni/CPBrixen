import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', 'Meet Joe Black', max_chars=7)
st.write('The current movie title is', title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'), help= 'click one of the three options')
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
 
# ! python3
import json, requests 

#add your own APIkey
APIkey = '6e1007dd818bd4d4dbd95b99a1ff01c7'
#location = st.text_input('Which city temperature?','London')
location = st.radio("Select one of these cities",('London', 'Paris', 'Amsterdam'), help= 'click one of the three options')

#check API documentation to see what structure of URL is needed to access the data
#http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
#print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
#print(response.text)  


#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
#print(weatherData) 
#from pprint import pprint 
#pprint(weatherData)  

st.text(str(weatherData['main']['temp_max']))
st.metric(label= 'temperature', 'C°')
# more???????????    
     
