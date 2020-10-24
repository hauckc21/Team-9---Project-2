# Import the functions we need from flask
from flask import Flask
from flask import render_template 
from flask import jsonify
from flask import request


# EL/CB Added the following:
from flask import request
from flask import json
from flask import url_for
import os


# Import the functions we need from SQL Alchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Define the database connection parameters
username = 'postgres'  # Ideally this would come from config.py (or similar)
password = 'bootcamp'  # Ideally this would come from config.py (or similar)
database_name = 'World_Alliance' 
connection_string = f'postgresql://{username}:{password}@localhost:5432/{database_name}'

# Connect to the database
engine = create_engine(connection_string)
base = automap_base()
base.prepare(engine, reflect=True)

# Choose the table we wish to use
alliances = base.classes.alliances
countries = base.classes.countries
details = base.classes.details

# Get Alliance_List
session = Session(engine)
alliance_list = session.query(alliances.full_name).all()
session.close()

# convert to list from list of tuples
alliance_list = [i[0] for i in alliance_list]

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
    # Check for arguments
    if request.args:
        # access the org number passed by the selector
        org_number = request.args.get('org')
        if org_number is not None:
            # index the alliance
            selected_alliance = alliance_list[int(org_number)]
    else:
        # default values
        selected_alliance = alliance_list[0]

    session = Session(engine)
     # query for matching alliance
    results = session.query(
            alliances.full_name, alliances.num_countries
        ).filter(
            alliances.full_name == selected_alliance
        ).all()[0]
    # package alliance data
    alliance_details = {'full_name': selected_alliance, 'num_countries': results[1]}

    # get country table for a selected_alliance
    results = session.query(
            countries
        ).filter(
            alliances.full_name == selected_alliance
        ).filter(
            details.alliances_id == alliances.alliances_id
        ).filter(
            countries.countries_id == details.countries_id
        ).all()

    session.close()

    country_details= [{'name': country.name, 
        'region': country.region, 
        'area': country.area,
        'population': country.population} 
        for country in results]   

    # add total population and area to alliance_details
    alliance_details['area'] = 0
    alliance_details['population'] = 0
    for country in country_details:
        alliance_details['area'] += country['area']
        alliance_details['population'] += country['population']

    # get rid of float adding error
    alliance_details['population'] = round(alliance_details['population'], 2)

    webpage = render_template("index.html", 
        alliance_list=alliance_list, 
        selected_alliance=alliance_details, 
        country_details=country_details)

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

# CB: Added flask route for map.html
@app.route('/map')
def map():
    webpage=render_template('map.html')
    return webpage
def IndexRoute():
#     """This function runs when the browser loads the index route"""
    webpage = render_template('index.html')
    return webpage

if __name__ == '__main__':
    app.run(debug=True)

