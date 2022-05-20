from flask import render_template, requests 
from . import main

@main.route('/')
def index():
    quotes=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    get_quotes=quotes.json()

    return render_template('main/index.html',get_quotes=get_quotes)

