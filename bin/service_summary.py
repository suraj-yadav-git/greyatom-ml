import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/home',methods = ['GET'])
def checkStatus():
    return "Service up and running.."

@app.route('/add',methods = ['GET'])
def addNum():
    a = 2
    b = 7
    return "Sum of {} and {} is {}".format(a, b, a+b)

app.run(host='localhost', port = 8012)