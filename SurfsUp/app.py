# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import app
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurements = Base.classes.measurement
Stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>" 
        f"/api/v1.0/stations<br/>" 
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/start<br/>" 
        f"/api/v1.0/start/end<br/>" 
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    earliest_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurements.date, 
                        Measurements.prcp).\
                  filter(Measurements.date >= earliest_date).\
                  order_by(Measurements.date).all()

    
    precipitation_list = {date: prcp for date, prcp in results}
    session.close()

    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    results = session.query(Stations.station).all()
    
    stations = list(np.ravel(results))
    #ssession.close()

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():     
    # Create our session (link) from Python to the DB
    earliest_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    station_tob = session.query(Measurements.tobs).\
                      filter(Measurements.station == 'USC00519281').\
                      filter(Measurements.date >= earliest_date).all()
    
    temperatures = list(np.ravel(station_tob))
    session.close()

    return jsonify(temperatures)

@app.route("/api/v1.0/<start>")
def trip1(start):

     # go back one year from start date and go to end of data for Min/Avg/Max temp   
    start = dt.datetime.strptime(start, '%Y-%m-%d')
    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).all()
    
    trip = list(np.ravel(trip_data))
    session.close()
    
    return jsonify(trip)

@app.route("/api/v1.0/<start>/<end>")
def trip2(start,end):

      # go back one year from start/end date and get Min/Avg/Max temp     
    start= dt.datetime.strptime(start, '%Y-%m-%d')
    end= dt.datetime.strptime(end,'%Y-%m-%d')
    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    
    trip = list(np.ravel(trip_data))
    session.close()
    
    return jsonify(trip)



if __name__ == '__main__':
    app.run(debug=True)