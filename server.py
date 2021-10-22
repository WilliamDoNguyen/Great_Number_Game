from flask import Flask, render_template, redirect, request, session
import random
from random import seed
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'wubba lubba dub dub'

random.seed(datetime.now())
num = random.randint(1, 100)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/restart', methods=['POST'])
def restart():
    session['random_numer'] = random.randint(1, 100)
    print(num)
    return redirect('/')

@app.route('/process_guess', methods=['POST'])
def guess():
    session['client_guess'] = int(request.form['guess'])
    return redirect('/guess')

@app.route('/guess')
def result():
    return render_template("guess.html", client_guess = session['client_guess'], random_number = num)

if __name__=="__main__":
    app.run(debug=True)
