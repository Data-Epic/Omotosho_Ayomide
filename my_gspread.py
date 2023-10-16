import gspread
import pandas as pd

# create a connection with the service account
gc = gspread.service_account("omotosho-project-c92e4f4bc071.json")
df = pd.read_csv("fileasa.csv")
spreadsheet = gc.open("Gspread practice")
# sh = gc.create('A new spreadsheet')

def get_or_create_worksheet(spreadsheet, Ecom , rows=1, cols=1):
    try:
        worksheet = spreadsheet.worksheet(Ecom)
    except:
        worksheet = spreadsheet.add_worksheet(Ecom, rows, cols)
    return worksheet

def populate_worksheet(Ecom):
    worksheet = get_or_create_worksheet(spreadsheet, Ecom, rows=df.shape[0]+1, cols=df.shape[1])
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())


populate_worksheet("Ecommerce store")
worksheet_list = spreadsheet.worksheets()
print(worksheet_list)
# worksheet= spreadsheet.worksheet("Ecommerce store")
# print(worksheet)