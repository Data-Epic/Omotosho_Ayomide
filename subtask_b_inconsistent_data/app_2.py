import pandas as pd
from datetime import datetime

df = pd.read_excel('subtask_b_inconsistent_data/inconsistent_data.xlsx')

def rename_column(df): 
    """
    Rename the 'S#' column to 'S/N'.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with renamed column
    """
    return df.rename(columns={"S#": "S/N"})

def drop_duplicate_rows(df):
    """
    Drop duplicate rows from the DataFrame.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data without duplicate rows
    """
    return df.drop_duplicates()

def fill_missing_values(df):
    """
    Fill missing values in various columns.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with filled missing values
    """
    df['Killed Min'].fillna(0, inplace=True)
    df['Injured Min'].fillna(0, inplace=True)
    df['No. of Suicide Blasts'].fillna(1, inplace=True)
    df['Explosive Weight (max)'].fillna(0, inplace=True)
    df['Killed Max'] = df['Killed Max'].fillna(method='bfill', axis=0)
    df['Explosive Weight (max)'] = df['Explosive Weight (max)'].str.replace(r'[^0-9.]', '', regex=True)
    return df

def change_dtype(df):
    """
    Change data types of various columns.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with changed data types
    """
    columns_to_int = ['Killed Min', 'Killed Max', 'Injured Min', 'No. of Suicide Blasts']
    for col in columns_to_int:
        df[col] = df[col].astype(int)
    
    df['Explosive Weight (max)'] = df['Explosive Weight (max)'].astype(float)
    return df

def parse_date(s):
    """
    Parse date strings into a consistent format.
    
    Args:
    - s (str): Original date string
    
    Returns:
    - str: Parsed date in '%Y-%m-%d' format
    """
    s = s.split("-", 1)[1]
    formats = ["%b %d-%Y", "%B %d-%Y", "%b-%d-%Y", "%B-%d-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    raise ValueError(f"Date {s} doesn't match known formats")

def apply_parse_date(df):
    """
    Apply date parsing function to the 'Date' column.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with parsed dates
    """
    df['Date'] = df['Date'].apply(parse_date)
    return df

def round_temperatures(df):
    """
    Round temperature values to 2 decimal places.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with rounded temperature values
    """
    df['Temperature(C)'] = df['Temperature(C)'].round(2)
    df['Temperature(F)'] = df['Temperature(F)'].round(2)
    return df

def convert_to_lowercase(df):
    """
    Convert strings in 'Islamic Date' column to lowercase.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with lowercase strings
    """
    df['Islamic Date'] = df['Islamic Date'].str.lower()
    return df
def remove_text(df):
    """
    removes the unit and other text for the explosive weight
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Data with lowercase strings
    """
    df['Explosive Weight (max)'] = df['Explosive Weight (max)'].astype(float).str.replace(r'[a-zA-Z]+$', '', regex=True)
    return df

# Load data
df = rename_column(df)
df = drop_duplicate_rows(df)
df = fill_missing_values(df)
df = change_dtype(df)
df = apply_parse_date(df)
df = round_temperatures(df)
df = convert_to_lowercase(df)
df = remove_text(df)

excel_file = "victims.xlsx"
df.to_excel(excel_file, index=False)

print(f"DataFrame has been exported to {excel_file}")