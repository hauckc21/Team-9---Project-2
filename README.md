
# **GLOBAL ALLIANCES & ORGANIZATIONS DASHBOARD** <BR> 
#### **`Visualizations to learn more about international alliances between member nations around the world!`**

***


<div style="text-align:center"><img src="static/images/G20-Summit-Communique-Flags.jpg" width="1000" height="300"/></div>



***
### **`TEAM MEMBERS: Eric Lewiston, Ken Njema, Chris Hauck, Colleen Banzhof`**<br>

***

### **PROJECT OVERVIEW: To create the dashboard our team performed the following steps**
***

**Step 1: `Data Scraping`** 
<br>
Our raw data was scraped from the following website into **`scrape_data.py`** using **`Python`** packages **`Beautiful Soup`** and **`Pandas`**:

- __https://www.worlddata.info/alliances/index.php__

**`== NOTE: API endpoint connection WAIT TIMES were very important to allow enough time to scrap the data! ==`**

After visiting each alliance URL, the dataset was narrowed down from 52 to 31 alliances based on the number of member countries of each alliance. 

<br>

**Step 2: `Data Cleaning`**
<br>
In **`Jupyter`** notebook, **`Pandas`** was used to perform the following steps to clean the data:<br>
- Selected and renamed relevant columns
- Dropped n/a's 
- Removed units from columns
- Re-formatted number columns as integer/float 
- Created 3 **`CSV files`**: Alliances, Countries, and Details

<br>

**Step 3: `Create PostgreSQL Database`** 
<br>
Because of the interrelation nature of the data between member states, where a single alliance could have more than one country or a country with more than one alliance, we chose to use **`PostgreSQL`**  because it is the most reliable of the relational open source databases. 


In **`PgAdmin`** we created a **`World Alliance database`** and three respective tables. The tables were populated by importing the **`csv files`** created during data cleaning and imported into **`PostgresSQL`** in the following order: Alliances.csv, Countries.csv, and Details.csv

<br>

**Step 4: `Establish Connection to Flask Server`** 
<br>

Via a **`Flask server`**, **`SQL Alchemy`** was used to connect to the **`PostgreSQL`** database. Values were populated using **`Java Script`** variables with **`Jinja2`** templating to pull the data from the **`PostgresSQL`** database into the website with a single **`API endpoint`** for all the three dashboard views.

<br>

**Step 5: `Create Webpage`**
<br>
The webpage was created using the following front-end coding languages:<br>
- **`HTML`**
- **`CSS`**
- **`Bootstrap`**

The landing page was created using an **`mp4 video`** as the header background embedded with a **`Learn More button`** to take the user to the  **`Visualization Dashboard`**.

<br>

**Step 6: `Create Interative Visualizations`**
<br>
The interactive visiualizations on the **`Visualization Dashboard`** were created using the following libraries:<br>
- A  **`D3 library`** (not covered in class) was used to create the spinning globe on the landing page by modifying starter code.<br>

- **`Leaflet / MapBox`** was used to create a 3-layered global map to plot member countries by alliance. When an alliance is selected from the drop down menu, a **`json`** plots map markers for each member country of the selected alliance on the map.<br>

- **`Apex Charts`** were used to create a table and pie chart. When an alliance is selected from the drop down menu, the table populates with the name of the selected alliance as well as the total number of member states, total land mass (km^2), and total population. Also based on the alliance selected from the drop down menu, the pie chart populates the percent each region represents in the alliance.

<br>

***

### **=== INSTRUCTIONS: Please follow the steps below to launch website ===**
***

`1. Create` **World_Alliance** `database in` **postgreSQL** 
- **REMINDER**: `Update your password in` **app.py**

`2. Use query tool to load` **World_Alliance.sql** `file`

`3. Run` **SQL** `code to create the tables`

`4. Import corresponding` **CSV files** `to each table in the following order:` **Alliances, Countries, Details**
- *TIP-1*: `For the` **Alliances & Countries CSV file** `import, locate file in static/data folder and select Headers (yes)`
- *TIP-2*: `For the` **Details CSV file** `import, deselect the details_id column from importing`

`5. Launch the` **app.py** `from git bash using source activate NewPythonData`

`6.` **ENJOY!**


*** 
### **SOURCES & ACKNOWLEDGMENTS**
***
* Primary Data Source for Webscraping: __https://www.worlddata.info/alliances/index.php__

* D3 Spinning Globe: Author - Sarah Schlotter. __https://observablehq.com/@sarah37/spinning-globe__

* Locations JSON: __http://techslides.com/list-of-countries-and-capitals__

* ApexCharts.js: __https://apexcharts.com/__

* Video Sources:
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __https://jsfiddle.net/StartBootstrap/enajc82d/__
 <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __https://mixkit.co/free-stock-video/international-flags-waving-in-the-wind-13129/__ 


