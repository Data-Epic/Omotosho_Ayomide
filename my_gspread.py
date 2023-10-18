import gspread
import pandas as pd
from dotenv import load_dotenv
import os 
import logging

load_dotenv()
API_key =  os.getenv('Project_key')

#create a connection
gc = gspread.service_account(API_key)

#read the data to be loaded
df = pd.read_csv("fileasa.csv")

#open the spreadsheet
spreadsheet = gc.open("Gspread practice")

logging.basicConfig(level=logging.INFO)

def get_or_create_worksheet(spreadsheet, ecom , rows=1, cols=1):
    '''
    This function gets a worksheet(Ecom) and if not found, it creates the worksheet

    :param spreadsheet: This is the spreadsheet which the worksheet is gotten from.
    :param ecom: This is the worksheet to get or create
    :param rows: This is the no of row initially created 
    :param col: This is the no of column initially created
    :return: The retrieved or newly created worksheet
    '''
    try:
        worksheet = spreadsheet.worksheet(ecom)
        logging.info("This worksheet already exist")
    except:
        worksheet = spreadsheet.add_worksheet(ecom, rows, cols)
        logging.info("The worksheet was not found, a new one will be created")
    return worksheet

def populate_worksheet(ecom):
    '''
    This function puts the header of a dataframe into the first row of a sheet followed by the values of a dataframe to the worsksheet that was created or already existing.
    
    :param ecom: The title of the worksheet to populate.
    '''
    # this worksheet is created based on the number of rows and column in the df
    worksheet = get_or_create_worksheet(spreadsheet, ecom, rows=df.shape[0]+1, cols=df.shape[1])
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    logging.info("The data has been successfully loaded into the spreadsheet")


populate_worksheet("Ecommerce store")