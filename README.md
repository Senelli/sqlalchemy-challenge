# sqlalchemy-challenge

## Jupyter Notebook Database Connection 
- Used the SQLAlchemy create_engine() function to connect the proper SQLite database used for this challenge
- Used the SQLAlchemy automap_base() function to reflect the tables into classes
- Saved references to the classes named station and measurement
- Linked Python to the database by creating a SQLAlchemy session
- Closed the session at the end of the notebook 

### Precipitation Analysis 
- Created a query that finds the most recent date in the dataset 
- Created a query that collects only the date and precipitation for the last year of data without passing the date as a variable 
- Saved the query results to a Pandas DataFrame to create date and precipitation columns
- Sorted the DataFrame by date 
- Plotted the results by using the DataFrame plot method with date as the x and precipitation as the y variables
- Used Pandas to print the summary statistics for the precipitation data

### Station Analysis
- Designed a query that correctly finds the number of stations in the dataset
- Designed a query that correctly lists the stations and observation counts in descending order and finds the most active station
- Designed a query that correctly finds the min, max, and average temperatures for the most active station
- Designed a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations
- Saved the query results to a Pandas DataFrame
- Correctly plotted a histogram with bins=12 for the last year of data using tobs as the column to count

## API SQLite Connection & Landing Page 
- Generated the engine to the correct sqlite file
- Used automap_base() and reflect the database schema
- Saved references to the tables in the sqlite file (measurement and station)
- Created and binded the session between the python app and database 
- Displayed the available routes on the landing page 

### API Static Routes 
- Created a Flask application that included the following:
    - A precipitation route that:
        - Returns json with the date as the key and the value as the precipitation
        - Only returns the jsonified precipitation data for the last year in the database 
    - A stations route that:
        - Returns jsonified data of all of the stations in the database 
    - A tobs route that:
        - Returns jsonified data for the most active station 
        - Only returns the jsonified data for the last year of data
    - A start route that:
        - Accepts the start date as a parameter from the URL 
        - Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset 
    - A start/end route that:
        - Accepts the start and end dates as parameters from the URL 
        - Returns the min, max, and average temperatures calculated from the given start date to the given end date 