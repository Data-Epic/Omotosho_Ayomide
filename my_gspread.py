import gspread
import pandas as pd
from dotenv_vault import load_dotenv
import os 

load_dotenv()
API_key =  os.getenv('Project_key')

gc = gspread.service_account(API_key)
df = pd.read_csv("fileasa.csv")
spreadsheet = gc.open("Gspread practice")

def get_or_create_worksheet(spreadsheet, Ecom , rows=1, cols=1):
    '''
    This function gets a worksheet(Ecom) and if not found, it creates the worksheet

    :param spreadsheet: This is the spreadsheet which the  worksheet is gotten from.
    :param Ecom: This is the worksheet to get or create
    :param rows: This is the no of row initially created 
    :param col: This is the no of column initially created
    :return: The retrieved or newly created worksheet
    
    '''
    try:
        worksheet = spreadsheet.worksheet(Ecom)
    except:
        worksheet = spreadsheet.add_worksheet(Ecom, rows, cols)
    return worksheet

def populate_worksheet(Ecom):
    '''
    This function puts the header of a dataframe into the first row of a sheet followed by the values of a dataframe to the worsksheet that was created or already existing.
    
    :param Ecom: The title of the worksheet to populate.
    '''
    worksheet = get_or_create_worksheet(spreadsheet, Ecom, rows=df.shape[0]+1, cols=df.shape[1])
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())


populate_worksheet("Ecommerce store")

#Prints the worksheet in the spreadsheet to check if the worksheet("Ecommerce store") has been created
worksheet_list = spreadsheet.worksheets()
print(worksheet_list)
