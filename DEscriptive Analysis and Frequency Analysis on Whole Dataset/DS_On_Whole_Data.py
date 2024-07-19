#%%
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the Excel file
data = pd.read_excel('datasetname.xlsx')

# Calculate the missing percentage for each column
missing_percentage = (data.isna().mean() * 100).round(2)

# Initialize lists to store statistics
statistics = {
    'Std': [],
    'Mean': [],
    'Median': [],
    '25%': [],
    '75%': [],
    'IQR': [],
    'Min': [],
    'Max': [],
    'Missing Count': [],
    'Missing %': []
}

# Iterate over each column to calculate statistics and generate plots
for column in data.columns:
    numeric_data = pd.to_numeric(data[column], errors='coerce').dropna()

    if not numeric_data.empty:
        # Calculate statistics
        statistics['Missing Count'].append(data[column].isna().sum())
        statistics['Missing %'].append(missing_percentage[column])
        statistics['Std'].append(numeric_data.std())
        statistics['Mean'].append(numeric_data.mean())
        statistics['Median'].append(numeric_data.median())
        statistics['25%'].append(numeric_data.quantile(0.25))
        statistics['75%'].append(numeric_data.quantile(0.75))
        statistics['IQR'].append(numeric_data.quantile(0.75) - numeric_data.quantile(0.25))
        statistics['Min'].append(numeric_data.min())
        statistics['Max'].append(numeric_data.max())


        # Visualization: Scatter plot, Box plot, and Histogram
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        axs[0].scatter(range(len(numeric_data)), numeric_data)
        axs[0].set_title(f'Scatter Plot of {column}')
        axs[1].boxplot(numeric_data, vert=True, patch_artist=True)
        axs[1].set_title(f'Box Plot of {column}')
        axs[2].hist(numeric_data, bins=20, color='skyblue', edgecolor='black')
        axs[2].set_title(f'Histogram of {column}')
        plt.show()
    else:
        # Append None for non-numeric or empty columns
        for key in statistics.keys():
            statistics[key].append(None)

# Convert statistics to a DataFrame and save to an Excel file
summary_df = pd.DataFrame(statistics, index=data.columns)
summary_df.to_excel('DS_Data_Summary.xlsx')
print("Analysis Complete")
# %%
