#%%
import pandas as pd
from scipy.stats import chi2_contingency

# Load data
data = pd.read_excel('datasetname.xlsx')

# Ensure the '# grant_3yr_checkin' is treated as a binary category
data['# grant_3yr_checkin'] = data['# grant_3yr_checkin'].astype(int)

# Filter data for analytic_set = 1
filtered_data = data[data['analytic_set'] == 1]

# Define the metric
metric = '# grant_3yr_checkin'

# Prepare the DataFrame for descriptive statistics
results = []


import pandas as pd

# Define a function to format the results
def format_results(counts):
    total = counts.sum()
    has_grants = counts.get(1, 0)  # Count of participants with grants
    no_grants = counts.get(0, 0)   # Count of participants without grants
    has_grants_percent = (has_grants / total * 100) if total else 0
    no_grants_percent = (no_grants / total * 100) if total else 0
    return f"{total} (Yes: {has_grants} - {has_grants_percent:.2f}%, No: {no_grants} - {no_grants_percent:.2f}%)"

# Calculate the counts for each group
total_grants = filtered_data['# grant_3yr_checkin'].value_counts()
group_1_grants = filtered_data[filtered_data['Pitt_Exit'] == 0]['# grant_3yr_checkin'].value_counts()
group_0_grants = filtered_data[filtered_data['Pitt_Exit'] == 1]['# grant_3yr_checkin'].value_counts()

# Calculate formatted results for each group
all_formatted = format_results(total_grants)
cim1_formatted = format_results(group_1_grants)
cim0_formatted = format_results(group_0_grants)

# Chi-square test for independence
chi2, p_value, _, _ = chi2_contingency(pd.crosstab(filtered_data['Pitt_Exit'], filtered_data['# grant_3yr_checkin']))

# Append results
results.append({
    'Metric': '# grant_3yr_checkin',
    'All N=238': all_formatted,
    'CIM=1 (Left Pitt)': cim1_formatted,
    'CIM=0 (Retained at Pitt)': cim0_formatted,
    'p-value': p_value
})

# Convert to DataFrame
final_results_df = pd.DataFrame(results)

# Output to Excel
final_results_df.to_excel('Categorical_Values_Descriptive_Statistics.xlsx', index=False)

