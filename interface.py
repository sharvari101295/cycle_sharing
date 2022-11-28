
from flask import Flask,jsonify,request,render_template
from project_app.utils import CycleSharing

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return render_template("home.html")
    
@app.route('/test')
def student():

    return render_template("index.html")
        
        
@app.route('/result', methods = ['POST', 'GET'])

def get_cycle_share_count():

    if request.method == 'POST':

        result = request.form

        season  = result['season']
        holiday = result['holiday']
        workingday = result['workingday']
        weather  = result['weather']
        temp  = result['temp']
        atemp  = result['atemp']
        humidity = result['humidity']
        windspeed = result["windspeed"]
        hour = result["hour"]
        day = result["day"]
        month = result["month"]
        year = result["year"]

        cycle_share = CycleSharing(season,holiday,workingday,weather,temp,atemp,humidity,windspeed,hour,day,month,year)
        cyclecount = cycle_share.get_cycle_share_count()

        return render_template("index.html", cyclecount = cyclecount)    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080,debug=True)  # server start