from flask import Flask, render_template,request
from eliza_function import bot,greet,username

app = Flask(__name__)


@app.route('/')
def home():
    bot_response='Welcome!'
    return render_template("home.html",bot_response=bot_response)

@app.route('/home',methods=['POST'])
def index():
    bot_response=greet()
    return render_template("index1.html",bot_response=bot_response)


@app.route('/logout',methods=['POST'])
def out():
    bot_response="Thank you for talking to me,Goodbye!"
    return render_template("index2.html",bot_response=bot_response)

@app.route('/user_name',methods=["GET", "POST"])
def user_name():
    user_input=request.form['user_input']
    bot_response = username(user_input)
    return render_template('index.html',user_input=user_input,bot_response=bot_response)


@app.route('/process',methods=["GET", "POST"])
def process():
    user_input=request.form['user_input']
    bot_response=bot(user_input)
    return render_template('index.html',user_input=user_input,bot_response=bot_response)

if __name__ == '__main__':
    app.run()

