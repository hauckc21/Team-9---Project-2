# Import the functions we need from flask
from flask import Flask
from flask import render_template 
from flask import jsonify

# Import the functions we need from SQL Alchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Define the database connection parameters
username = 'postgres'  # Ideally this would come from config.py (or similar)
password = 'Jahpeople'  # Ideally this would come from config.py (or similar)
database_name = 'World_Alliance' # Created in Week 9, Night 1, Exercise 08-Stu_CRUD 
connection_string = f'postgresql://{username}:{password}@localhost:5432/{database_name}'

# Connect to the database
engine = create_engine(connection_string)
base = automap_base()
base.prepare(engine, reflect=True)
base.classes.keys()


# Choose the table we wish to use
alliances = base.classes.alliances
countries = base.classes.countries
details = base.classes.details

# Instantiate the Flask application. (Chocolate cake recipe.)
# This statement is required for Flask to do its job. 
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching

# Here's where we define the various application routes ...
@app.route("/test")
def TestRoute():
    ''' This function returns a simple message, just to guarantee that
        the Flask server is working. '''

    return "This is the test route!"

@app.route("/")
def IndexRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''

    webpage = render_template("index.html")
    return webpage

@app.route("/alliances")
def alliances_results():
    ''' Query the database for alliances and return the results as a JSON. '''

    # Open a session, run the query, and then close the session again
    session = Session(engine)
    results = session.query(alliances.full_name, alliances.num_countries).all()
    
    session.close()

# Create a list of dictionaries, with each dictionary containing one row from the query. 
    all_alliances = []
    for full_name, num_countries in results:
        dict = {}
        dict["full_name"] = full_name
        dict["num_countries"] = num_countries
        all_alliances.append(dict)
    print(all_alliances)

    #Return the jsonified result. 
    return jsonify(all_alliances)

@app.route("/countries")
def countries_results():
    ''' Query the database for alliances and return the results as a JSON. '''

    # Open a session, run the query, and then close the session again
    session = Session(engine)


    results = session.query(countries.countries_id, countries.name, countries.region, countries.area, countries.population).all()

    session.close()

# Create a list of dictionaries, with each dictionary containing one row from the query. 
    all_countries = []
    for countries_id, name, region, area, population in results:
        dict = {}
       
        dict["countries_id"] = countries_id
        dict["name"] = name
        dict["region"] = region
        dict["area"] = area
        dict["population"] = population
        all_countries.append(dict)
    print(all_countries)

    #Return the jsonified result. 
    return jsonify(all_countries)

@app.route("/details")
def details_results():
    ''' Query the database for details and return the results as a JSON. '''

    # Open a session, run the query, and then close the session again
    session = Session(engine)
    results = session.query(details.details_id, details.alliances_id, details.countries_id).all()

    session.close()

# Create a list of dictionaries, with each dictionary containing one row from the query. 
    all_details = []
    for details_id, alliances_id, countries_id in results:
        dict = {}
       
        dict["details_id"] = details_id
        dict["alliances_id"] = alliances_id
        dict["countries_id"] = countries_id
        
        all_details.append(dict)

    print(all_details)

    #Return the jsonified result. 
    return jsonify(all_details)


if __name__ == '__main__':
    app.run(debug=True)

