# Data Cleaning Process

## **Missing Data Transformations**

Here are the transformations performed on the missing data file:

1. **Drop Columns**: Removed columns with missing values greater than 13,000, as they aren't suitable for analysis due to the high number of null values.
2. **Street Suffix**: Populated this with values from preceding rows since there are roughly five categories for street suffixes.
3. **Cost Columns**: Filled null values in the `Revised Cost` and `Estimated Cost` with their respective column averages.
4. **Location-Related Columns**: Populated `Location`, `Zipcode`, `Neighborhoods - Analysis Boundaries`, and `Supervisor District` using values from subsequent rows.
5. **Construction Type Columns**: 
   - Set `Existing Construction Type` and `Proposed Construction Type` to '0', as they were empty due to unissued constructions.
   - Populated `Existing Construction Type Description` and `Proposed Construction Type Description` with "No Description for this construction" since the associated construction type was null.
6. **Date Columns**:
   - Populated missing `Completion Date` values with the latest date, assuming all constructions were completed by then.
   - Used the earliest date for missing `Issue Date` values, assuming constructions started before that time.
   - Set `Permit Expiration Date` null values to the most recent date as the last expiration date.
   - Populated missing `First Construction Document Date` with the latest date.
7. **Others**:
   - Set the `Number of Existing Stories`, `Plansets`, `Proposed Units`, and `Number of Proposed Stories` to 0 for unissued constructions.
   - Populated `Existing Use` with "No existing use yet" and `Proposed Use` with "No proposed use yet".
8. **Export**: The cleaned data was saved as an Excel file named "construction".

## **Inconsistent Data Transformations**

1. **Column Rename**: Changed the "s#" column name to "SN".
2. **Duplicate Rows**: Removed any potential duplicate rows.
3. **Injury and Death Columns**: 
   - Populated `Injure Min` and `Killed Min` with 0 as the lowest possible value.
   - Used values from `Killed Min` to populate `Killed Max`, ensuring the latter is always greater.
   - Modified the data type for `Killed Min`, `Killed Max`, `Injure Min`, and `Injured Max` to integer.
   - Set `No. of Suicidal Blast` to 1, assuming a minimum of one bomber.
4. **Date and Time**: Converted time by identifying the various formats present in the dataframe.
5. **Text Transformations**:
   - Converted `Islamic Date` to lowercase.
   - Rounded temperature values to three decimal places.
   - Removed non-numeric characters from `Explosive Weight` and converted the cleaned data to float.

6. **Export**: The cleaned data was saved as an Excel file named "victims"