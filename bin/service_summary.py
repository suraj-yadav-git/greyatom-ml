import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def checkStatus():
    return "Service up and running.."

@app.route('/get_summary', methods = ['GET'])
def getSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run(host='localhost', port = 8012)