from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dress/')
def dress():
    return render_template('dress.html')

@app.route('/bot/')
def bot():
    return render_template('bot.html')

@app.route('/kyrtka/')
def kyrtka():
    return render_template('kyrtka.html')

if __name__ == '__main__':
    app.run(debug=True)
