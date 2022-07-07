from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def handleResponse():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        data = request.json
        return jsonify(data)


    

#parameters: time of day, what im doing, 
