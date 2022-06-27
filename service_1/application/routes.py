from application import app
from flask import render_template
import requests #lets us grab data from http
from random import randint

#this is the main route, that nginx will direct to
@app.route('/')
def index():
    obj = requests.get('http://service_2:5000/rand_1').text
    source = requests.get('http://service_3:5000/rand_2').text
    name = requests.post('http://service_4:5000/prize', json=dict(obj=obj, source=source))

    return render_template('home.html', name = name.text, obj = obj, source = source)
    #rand_1 = requests.get('http://service_2:5000/rand_1')
    #final = requests.post('http://service_4:5000/final)
    #because it's a post request it also accepts info back 
    #so we can assign that to a variable
    #we then render the home template and pass in our variables above
    #it's important to decode the stuff you pass accross with html requests
    
#PUT IT HERE
#essentially we just return a value and then it'll be captured in routes of service 1