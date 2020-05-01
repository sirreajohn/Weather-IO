from flask import Flask,render_template
from flask import request
from ip2geotools.databases.noncommercial import DbIpCity
from requests import get 
import json
from darksky.api import DarkSky
from darksky.types import units,languages,weather
#get all libraries first 
#i suggest using VScode for editing 
app = Flask(__name__)

#tarak, this function for getting ip address
def ipad():
    ip_address = request.remote_addr
    return ip_address

def weatherinfo(lat,long_):
    api ='af654ddc453104adcc9b4d0818a7604d'
    dsky = DarkSky(api)
    forecast = dsky.get_forecast(
        lat,long_,
        extend=False,
        lang=languages.ENGLISH,
        values_units= units.SI,
        exclude=[weather.MINUTELY,weather.HOURLY,weather.ALERTS,weather.FLAGS]
    )
    return forecast

@app.route("/")
def home():
    ip = '106.208.38.24' #this is random ip...for real ip call ipad() here 
    response = DbIpCity.get(ip,api_key = 'free')
    forecast = weatherinfo(response.latitude,response.longitude)
    
    
    #variables for display , ready to display 

    temperature = forecast.currently.temperature
    summary = forecast.currently.summary
    humidity = forecast.currently.humidity
    windspeed = forecast.currently.humidity
    ozone = forecast.currently.ozone
    pressure = forecast.currently.pressure
    #pass the variables here first to diaplay 
    return render_template('mahesh.html',tempvar = temperature,summaryvar = summary,humidityvar =humidity,windspeedvar = windspeed,ozonevar = ozone,pressurevar = pressure )


if __name__ == "__main__":
    app.run(debug = True)