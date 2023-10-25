import pytest
import gspread
import pandas as pd
from pandas import json_normalize
from dotenv import load_dotenv
import os
import requests
import json
import datetime as dt

from my_gspread import get_or_create_worksheet
from my_gspread import pass_json_into_df

load_dotenv()
gspread_key = os.getenv('Project_key')
gc = gspread.service_account(gspread_key)
spreadsheet = gc.open("Gspread practice")
wk = spreadsheet.worksheet("Weather")
# Initialize your Weather API key (assuming it's correctly set in your environment)
Weather_API = os.getenv('API_key')
with open(Weather_API) as json_data_file:
    config = json.load(json_data_file)


payload = {'Key': config['Key'], 'q': 'berlin', 'aqi': 'no'}
r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)

def test_for_successful_worksheet_creation():
    '''
    This test for the spreadsheet title and worksheet title, it also test to see if there are values in the worksheet
    '''
    worksheet_name = "Weather"
    worksheet = get_or_create_worksheet(spreadsheet,"Weather")
    
    assert worksheet is not None
    assert worksheet.title == worksheet_name
    assert spreadsheet.title == 'Gspread practice'
    assert worksheet.row_count != 0

def test_for_connection_with_API():
    '''
    This test for the successful connection with the weather API, by checking the response state code
     '''
    payload = {'Key': config['Key'], 'q': 'berlin', 'aqi': 'no'}
    r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)
    assert r.status_code == 200
    assert r.status_code != 400
    assert r.status_code != 500

def test_for_column_names():
    '''
    This test for the if the right column names is present in the columns of the dataframe
    '''
    df = pass_json_into_df(r)
    expected_columns = ['timestamp', 'location', 'state', 'country', 'temp_c', 'wind_kph', 'latitude', 'longitude', 'wind_direction']
    assert len(df.columns) == len(expected_columns)
    assert "location" in df.columns, "Missing column 'location'"
    assert "state" in df.columns, "Missing column 'state'"
    assert "country" in df.columns, "Missing column 'country'"
    assert "timestamp" in df.columns, "Missing column 'timestamp'"
    assert 'wind_direction' in df.columns, "Missing column 'wind_direction'"
    assert 'temp_c' in df.columns, "Missing column 'temp_c'"
    assert 'wind_kph' in df.columns, "Missing column 'wind_kph'"
    assert 'latitude' in df.columns, "Missing column 'latitude'"
    assert 'longitude' in df.columns, "Missing column 'longitude'"
    assert 'wind_direction' in df.columns, "Missing column 'wind_direction'"

def test_for_column_datatypes(sample_dataframe):
    '''
    This test checks the data types of columns in the DataFrame.
    '''
    df = pass_json_into_df(r)
    assert df['location'].dtype == 'object', "Column 'location' should have data type 'object'"
    assert df['state'].dtype == 'object', "Column 'state' should have data type 'object'"
    assert df['country'].dtype == 'object', "Column 'country' should have data type 'object'"
    assert df['timestamp'].dtype == 'object', "Column 'timestamp' should have data type 'object'"
    assert df['wind_direction'].dtype == 'object', "Column 'wind_direction' should have data type 'object'"
    assert df['temp_c'].dtype == 'float64', "Column 'temp_c' should have data type 'float64'"
    assert df['wind_kph'].dtype == 'float64', "Column 'wind_kph' should have data type 'float64'"
    assert df['latitude'].dtype == 'float64', "Column 'latitude' should have data type 'float64'"
    assert df['longitude'].dtype == 'float64', "Column 'longitude' should have data type 'float64'"

def test_for_data_validation():
    '''
    This test checks if data in certain columns falls within valid ranges
    '''
    df = pass_json_into_df(r)
    assert (df['temp_c'] >= -100).all(), "Invalid temperature values"
    assert (df['temp_c'] <= 100).all(), "Invalid temperature values"
    assert (df['wind_kph'] >= 0).all(), "Invalid wind speed values"
    assert (df['wind_kph'] <= 300).all(), "Invalid wind speed values"