from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
engine = create_engine("sqlite:///Desktop/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
dates_2017 = session.query(Measurement).\
    filter(Measurement.date > 2017)

precipitation_list = []
date_list = []

for measurements in dates_2017:
    precipitation_list.append(measurements.prcp)

for measurements in dates_2017:
    date_list.append(measurements.date)

precipitation_dict = {"Precipitation": precipitation_list}

df = pd.DataFrame(data=precipitation_dict, index=date_list)

df.index.name = "Date"

d = dict(zip(date_list, precipitation_list))

Measurement_query = session.query(Measurement)

station_list = []

for measurements in Measurement_query:
    station_list.append(measurements.station)

observations = session.query(Measurement).\
    filter(Measurement.date > 2017)

observation_list = []

for measurement in observations:
    observation_list.append(measurement.tobs)

observation_list



#This is where Activity 2 actually starts
from flask import Flask, jsonify

new_app = Flask(__name__)


@new_app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "These are the routes available: "


@new_app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server recieved request for 'precipitation' page...")
    return jsonify(d)


@new_app.route("/api/v1.0/stations")
def stations():
    print("Server recieved request for 'stations' page...")
    return jsonify(station_list)

@new_app.route("/api/v1.0/tobs")
def tobs():
    print("Server recieved request for 'tobs' page...")
    return jsonify(observation_list)

@new_app.rout("/api/v1.0/<start>")
def start():
    print("Server recieved request for 'start' page...")
    return
