import pandas as pd
import datetime

def main():
    """
    Main function to load the data, perform transformation and save the results.
    
    Returns:
    - DataFrame: The transformed DataFrame
    """
    df = pd.read_excel('Subtask_A_missing_values/Intermediate_Task.xlsx')  # Load the data
    df2 = fill_missing_values()  # Fill missing values and transform the data
    excel_file = "construction.xlsx"  # Name of the output Excel file
    df2.to_excel(excel_file, index=False)  # Save the DataFrame to an Excel file
    print(f"DataFrame has been exported to {excel_file}")  # Print the export confirmation message
    return df

def drop_columns_transformation(df):
    """
    Drop columns from the DataFrame based on a certain threshold of missing values.
    
    Args:
    - df (DataFrame): Original data
    
    Returns:
    - DataFrame: Transformed data with certain columns dropped
    """
    threshold = 13000  # Define a threshold for missing values
    # Find columns with missing value rate higher than threshold
    cols_to_drop = df.columns[df.isnull().sum() > threshold]
    df2 = df.drop(columns=cols_to_drop)  # Drop identified columns
    return df2

def fill_missing_values():
    """
    Fill missing values in various columns of the DataFrame.
    
    Returns:
    - DataFrame: Transformed data with missing values filled
    """
    df = main()  # Load the main DataFrame
    df2 = drop_columns_transformation(df)  # Drop columns based on missing values threshold
    
    # Handle missing values for 'Completed Date', 'Issued Date' and 'Permit Expiration Date'
    for col, func in [('Completed Date', max), ('Issued Date', min), ('Permit Expiration Date', max), ('First Construction Document Date', max)]:
        df2[col] = pd.to_datetime(df2[col], errors='coerce')  # Convert to datetime
        date_func_value = func(df2[col])  # Find the date (highest or lowest based on the function)
        df2[col].fillna(date_func_value, inplace=True)  # Fill missing values
    
    # Define default fill values for certain columns
    fill_values = {
        'Existing Construction Type': 0,
        'Existing Construction Type Description': 'No Description for this construction type',
        'Proposed Construction Type': 0,
        'Proposed Construction Type Description': 'No Description for this construction type',
    }
    df2.fillna(fill_values, inplace=True)  # Fill missing values based on the defined dictionary
    
    # Other column-specific missing value handling
    df2["Revised Cost"].fillna(df2["Revised Cost"].mean(), inplace=True)
    df2['Description'] = df2['Description'].fillna('No description available for this product')
    df2['Street Suffix'] = df2['Street Suffix'].fillna(method='pad')
    
    # Calculate the mean of the "Number of Existing Stories" column as an integer
    mean_existing_stories = int(df['Number of Existing Stories'].mean())
    df2['Number of Existing Stories'].fillna(mean_existing_stories, inplace=True)

    # Fill zeros for certain columns
    for col in ['Number of Proposed Stories', 'Proposed Units', 'Existing Units', 'Plansets']:
        df2[col].fillna(0, inplace=True)

    df2['Existing Use'].fillna("No Existing Use yet", inplace=True)
    df2["Estimated Cost"].fillna(df2["Estimated Cost"].mean(), inplace=True)
    df2['Proposed Use'].fillna("No Proposed Use yet", inplace=True)
    
    return df2

if __name__ == "__main__":
    main()
