#%%
import pandas as pd

# Load your dataset from the Excel file
df = pd.read_excel('datasetname.xlsx')

# Define groups of columns for different sheets
column_groups = {
    'Sheet1': [
        'Found link to CV (saved in Master)',
        'Found link to Public Profile (saved in Master)',
        'Y/N Found Postdoc Mentor (saved in Master)'
    ],
    'Sheet2': [
        'FIS_Nationality',
        'URM',
        'Gender'
    ]
}

# Create an Excel writer
with pd.ExcelWriter('Frequency_tables.xlsx', engine='xlsxwriter') as excel_writer:
    # Iterate over the column groups
    for sheet_name, columns in column_groups.items():
        # Create an empty DataFrame to store the frequency tables
        frequency_tables_df = pd.DataFrame(columns=['Column', 'Value', 'Frequency', 'Percent', 'Cumulative Frequency', 'Cumulative Percent', 'Missing'])

        # Iterate over the columns to be analyzed in the group
        for column in columns:
            # Create a frequency table for the column
            frequency_table = df[column].value_counts().reset_index(name='Frequency')
            frequency_table.columns = ['Value', 'Frequency']

            # Add a column for the 'Percent' measure
            frequency_table['Percent'] = (frequency_table['Frequency'] / len(df) * 100).round(2)

            # Add a column for the number of missing values
            missing_count = df[column].isna().sum()
            frequency_table['Missing'] = missing_count

            # Add a column for the cumulative frequency
            frequency_table['Cumulative Frequency'] = frequency_table['Frequency'].cumsum()

            # Calculate the cumulative percentage
            frequency_table['Cumulative Percent'] = (frequency_table['Cumulative Frequency'] / len(df) * 100).round(2)

            # Reorder the columns
            frequency_table = frequency_table[['Value', 'Frequency', 'Percent', 'Cumulative Frequency', 'Cumulative Percent', 'Missing']]

            # Add a column for the 'Column' name
            frequency_table.insert(0, 'Column', column)

            # Append the frequency table to the combined DataFrame
            frequency_tables_df = pd.concat([frequency_tables_df, frequency_table])

        # Save the frequency tables directly to the Excel file
        frequency_tables_df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

print("Complete")
