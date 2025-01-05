# Import needed functions from flask
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
password = 'Subs1200'  # Ideally this would come from config.py (or similar)
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

@app.route("/")
def IndexRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''

    webpage = render_template("index.html")

    return webpage

# CB: Added flask route for map.html
@app.route('/map')
def map():
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

    webpage = render_template('map.html', 
        alliance_list=alliance_list, 
        selected_alliance=alliance_details, 
        country_details=country_details)

    return webpage


if __name__ == '__main__':
    app.run(debug=True)

