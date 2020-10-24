
# **GLOBAL ALLIANCE DASHBOARD** <BR> 
### `Visualizations for international alliances between member nations across the globe`

***


<div style="text-align:center"><img src="static/images/G20-Summit-Communique-Flags.jpg" width="1000" height="300"/></div>



***
### **TEAM MEMBERS: Eric Lewiston, Ken Njema, Chris Hauck, Colleen Banzhof**<br>

***

### **PROJECT OVERVIEW: To create the dashboard our team performed the following steps**
***

**Step 1: `Data Scraping`** - TO DO: EDIT THE FOLLOWING --> Our raw data was scraped from the following website into **`scrape_data.py`**:

- __https://www.worlddata.info/alliances/index.php__


**`== IMPORTANT: Once an API endpoint connection was established, wait times were built in to allow enough time to scrap the data.==`**

<br>

**Step 2: `Data Cleaning`** - TO DO: EDIT THE FOLLOWING --> Get/clean data (Beautiful Soup, Pandas, Python)

After cleaning the data, two CSV files were created and imported into into Python for additional cleaning including selecting and renaming relevant columns and dropping n/a's.

<br>

**Step 3: `Create PostgreSQL Database`** - TO DO: EDIT THE FOLLOWING --> Database tables and relationships (PostgreSQL)

Because of the interrelation nature of the data between member states, where a single alliance could have more than one country or a country with more than one alliance, we chose to use PostgreSQL because it is the most reliable of the relational Open Source databases. 


In PgAdmin we created a World Alliance database and three respective tables were populated with the data imported from the csv files from the web scraping and data cleaning were imported into Postgres in the following order: Alliances.csv, Countries.csv, and Details.csv

Finally, we included a Flask server to pull the data from the Postgre database to the website with a single API endpoint for all the three dashboard views.

<br>

**Step 4: `Establish Connection to Flask Server`** - TO DO: EDIT THE FOLLOWING --> Flask server/API (Python, Flask)

ABCD


<br>

**Step 5: `Create Webpage`** - TO DO: EDIT THE FOLLOWING -->Website (HTML/CSS/Bootstrap)


**Step 6: `Create Graphs/Maps`** - TO DO: EDIT THE FOLLOWING --> (JavaScript: D3/Plotly/Leaflet/other library)

**FINAL STEP PLACEHOLDER: `Presentation`** - (Power Point/Live website demo)

<br>

***

### **=== INSTRUCTIONS: Please follow the steps below to recreate Database ===**
***
TO DO: EDIT THE FOLLOWING --> REMINDER FROM DOM: JS talks to flask & flask talks to DB` delete

`1. Establish connection to` **Flask Server** 

`2. Launch` **index.html** `file`

`3. `

*** 
### **SOURCES & ACKNOWLEDGMENTS**
***
* Primary Data Source for Webscraping: __https://www.worlddata.info/alliances/index.php__

* D3 geoOrthographic to geoMercator Globe: Author - Rich Yap. __https://observablehq.com/@richdayandnight/spinning-globe-changes-projection-from-d3-geoorthographi__

* Image Data Sources: __https://www.shutterstock.com/__

* Webpage Background Image: <span>Photo by <a href="https://unsplash.com/@nasa?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">NASA</a> on <a href="https://unsplash.com/s/photos/abstract-background?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<!-- * JavaScript library not covered in class:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flag Icon Library: __https://cdnjs.com/libraries/flag-icon-css,  https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.5.0/css/flag-icon.min.css__ -->