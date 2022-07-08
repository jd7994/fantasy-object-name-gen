from application import app
from flask import render_template
import requests #lets us grab data from http
from random import randint

#this is the main route, that nginx will direct to
@app.route('/')
def home():
    obj = requests.get('http://service_2:5000/rand_1').text
    source = requests.get('http://service_3:5000/rand_2').text
    
    #because it's a post request it also accepts info back 
    #so we can assign that to a variable
    name = requests.post('http://service_4:5000/final', json={"obj": obj, "source": source})
    #we then render the home template and pass in our variables above
    #it's important to decode the stuff you pass accross with html requests
    return render_template('home.html', name = name.text, obj = obj, source = source)
  
    
    
    
