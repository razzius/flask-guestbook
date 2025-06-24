from flask import Flask, render_template, request

app = Flask(__name__)

guests = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        guests.append(request.form['name'])

    return render_template('home.html', guests=guests)
