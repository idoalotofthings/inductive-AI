from flask import Flask, request
from model_driver import bot
import json

app = Flask(__name__)

@app.route("/ai", methods = ["POST"])
def model_endpoint():
    if request.method == "POST":
        _json = json.loads(request.get_data())
        print(_json)
        question = _json["question"]
        answer = bot.question_model(question)
        return f'{{"answer":"{answer}"}}'
    else:
        return '{ "status":"error", "message":"Only JSON format is supported"'
    
if __name__ == "__main__":
    app.run() 
