# Populating an excel sheet with Gspread library

## Overview

This project allows you to upload the contents of a Pandas DataFrame to a Google Sheet using the gspread library. Specifically, it checks if a worksheet with a specified title exists in the spreadsheet. If the worksheet doesn't exist, it creates one. It then populates the worksheet with the headers and values from the DataFrame.


## Tools Used
The following tools were used in this project:
   - Python
   - Gspread library
   - Pandas library
   - Dotenv

##  Data Source
The data used was the first 500 rows of a dataset obtained from Kaggle. click on this [link](https://www.kaggle.com/datasets/lissetteg/ecommerce-dataset) to access the file.

## Prerequisites

Before using this script, ensure you have the following prerequisites in place:

1. **Python:** This script is written in Python. You will need Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Required Python Packages:** You need to install the following Python packages if they are not already installed:

   - `gspread`: For interacting with Google Sheets.
   - `pandas`: For data manipulation with DataFrames.
   - `dotenv`: For loading environment variables from a .env file.
   - `logging`: for generating logs after the script has been executed.

   You can install these packages using `pip`:

   ```
   pip install gspread pandas python-dotenv
   ```

3. **Google Sheets API Key:** You need to obtain a Google Sheets API key for authentication. The key should be stored as an environment variable. Create a `.env` file in the same directory as your script and add the API key as follows:

   ```
   Project_key=YOUR_API_KEY
   ```

4. **CSV Data File:** Prepare the CSV file containing the data you want to upload. Make sure the CSV file is in the same directory as your script.(the assumption)

## Usage

- **Edit Worksheet Name:** Modify the `populate_worksheet` function by changing the argument to the desired worksheet name. For example, if you want to upload data to a worksheet named "Data Epic team" use:

   ```
   populate_worksheet("Data Epic team")
   ```


## Script Explanation

- The script begins by loading the necessary libraries and reading the data from the CSV file specified in `pd.read_csv("fileasa.csv")`.

- It establishes a connection to the Google Sheets API using the API key stored in the `.env` file.

- The `get_or_create_worksheet` function checks if the target worksheet (specified as "Ecommerce Store" in the example) exists in the spreadsheet. If it does not exist, it creates a new worksheet with the given name. This function also ensures that the worksheet has the appropriate number of rows and columns to accommodate the data from the CSV file.

- The `populate_worksheet` function uploads the data from the CSV file into the specified worksheet. It first writes the column headers from the DataFrame to the first row of the worksheet, followed by the data.

- The script uses logging to provide information about the execution process, including whether the worksheet already exists or if a new one is created.



## Author

 - Omotosho Ayomide
 Email: Ayomidemtsh@gmail.com



 ## Spreadsheet link
 
Here is a [link to the spreadsheet](https://docs.google.com/spreadsheets/d/1CpGvA2oy0FOdC-IdyFeO2JDkaiWxY9sX1cO6Vl8Zz04/edit?usp=sharing)  