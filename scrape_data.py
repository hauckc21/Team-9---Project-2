import requests
import time
import sys
from random import randint
import pandas as pd
from bs4 import BeautifulSoup
from config import table_urls


def check_status(status_code):
    """Checks for too many requests code, exits if found"""
    if status_code == 429:
        input("Too many requests, try again later")
        sys.exit()


base_url = 'https://www.worlddata.info'

alliances_url = '/alliances/index.php'

# fake headers for browsing
headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}

r = requests.get(base_url + alliances_url, headers=headers)

check_status(r.status_code)

# get alliances table
alliances_df = pd.read_html(r.text)[0]

# Due to the wait times necessary to not trigger a 429, this will take approximately 7-13 minutes to run
alliance_details = []
for rel_url in table_urls.values():
    print(f"Scraping {base_url + rel_url}")

    # wait to avoid triggering "too many requests" from website
    time.sleep(randint(15,25))
    
    # access webpage
    r = requests.get(base_url + rel_url, headers=headers)
    check_status(r.status_code)
    
    # extract first table
    group_df = pd.read_html(r.text)[0]
    
    # select columns
    cols = ['Country', 'Region', 'Area', 'Population']
    group_df = group_df[cols]
    
    # replace units and commas
    group_df.Area = group_df.Area.str.replace(' km²', '', regex=False)
    group_df.Area = group_df.Area.str.replace(',', '', regex=False)
    # replace units and commas
    group_df.Population = group_df.Population.str.replace(' M', '', regex=False)
    group_df.Population = group_df.Population.str.replace(',', '', regex=False)
    
    # set types
    group_df = group_df.astype({'Area': 'int64', 'Population':'float64'})
    
    alliance_details.append(group_df)
    
# ******************************************************************
# Get countries unique countries and save as csv

# combine all dfs
countries_df = pd.concat(alliance_details)
# remove duplicates
countries_df.drop_duplicates(inplace=True)

countries_df.sort_values(by='Country', inplace=True)

# reset the indices from the combined data frames
countries_df.reset_index(drop=True, inplace=True)
# name index and columns to match db table names
countries_df.index.rename(name='countries_id', inplace=True)
countries_df.rename(columns={'Country': 'name', 'Region': 'region', 'Area': 'area', 'Population': 'population'}, inplace=True)

print("Writing countries.csv")

countries_df.to_csv('Static/data/countries.csv')

# ******************************************************************
# Compare alliances table with those we're actually using, save as csv

# based on config.py, create a mask for the alliances table
mask = [row['Name'] in [*table_urls] for index, row in alliances_df.iterrows()]
# filter alliances by mask
alliances_df = alliances_df.loc[mask]

alliances_df.reset_index(drop=True, inplace=True)

# name index and columns to match db table names
alliances_df.index.rename(name='alliances_id', inplace=True)
alliances_df.rename(columns={'Name': 'full_name', 'Countries': 'num_countries'}, inplace=True)

print("Writing alliances.csv")

alliances_df.to_csv('Static/data/alliances.csv')

# ******************************************************************
# Get alliance and country indicies to populate details csv

for idx, df in enumerate(alliance_details):
    # add alliances_id column
    df['alliances_id'] = idx
    
    # add countries_id column based on loc in countries_df
    df['countries_id'] = pd.Series([countries_df[countries_df['name'] == row['Country']].index.values[0] for index, row in df.iterrows()])
    
    # drop extra columns
    df.drop(columns=['Country', 'Region', 'Area', 'Population'], inplace=True)
# concat all dfs
details_df = pd.concat(alliance_details)

# SADC has Zimbabwe listed twice, so we drop that here
details_df.drop_duplicates(inplace=True)

print("Writing details.csv")

# save without index
details_df.to_csv('Static/data/details.csv', index=False)