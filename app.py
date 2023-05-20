from flask import Flask, render_template, jsonify

app = Flask(__name__)

QUES=[{
    'qno':1,
    'q':'You are a legend'
},
{
    'qno':2,
    'q':'what is your name'
},
{
    'qno':3,
    'q':'what is your problem'
},
{
    'qno':4,
    'q':'pls leave me alone'
},
{
    'qno':5,
    'q':'you are a shit'
}]

@app.route('/')
def hello():
    return render_template('login.html',ques=QUES)

@app.route('/api/question')
def list_ques():
    return jsonify(QUES)
