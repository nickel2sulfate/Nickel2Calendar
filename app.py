from flask import Flask, request, jsonify, render_template
from main import generateScheduleImages
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def handleResponse():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        data = request.json
        generateSchedule(data)
        return jsonify(data)

@app.route("/custom-message.html",methods=['GET'])
def handleSettings():
    if request.method == 'GET':
        return render_template('custom-message.html')
        
def generateSchedule(data):
    times = []
    things = []
    for day in data:
        times.append(day["time"])
        things.append(day["category"])
    #if nothing is written in times or things
    times = [value + " EST" if value else "--" for value in times]
    things = [value if value else "--" for value in things]
    #return(times, things)
    generateScheduleImages(times,things)


app.run(debug=True)

    

#parameters: time of day, what im doing, 
