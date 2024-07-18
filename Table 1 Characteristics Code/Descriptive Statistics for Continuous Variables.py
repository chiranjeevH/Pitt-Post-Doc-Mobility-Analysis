#%%
import pandas as pd
from scipy.stats import mannwhitneyu
import numpy as np

# Load data
data = pd.read_excel('datasetname.xlsx')

# Convert all potentially numeric columns explicitly and handle errors
def safe_convert_to_numeric(column):
    try:
        return pd.to_numeric(column, errors='coerce')
    except:
        return np.nan

# Apply conversion to all columns that should be numeric
numeric_columns = [
    '# of Pubs from end of postdoc to 3-year check-in', 
    'H-Index ever up to 3 year check-in', 
    'Cat. Normal Citation Impact ever up to 3-year check-in', 
    '# of 1st Author Pubs from end of postdoc to 3-year check-in',
    '% of 1st Author Pubs from end of postdoc to 3-year check-in',
    '# of last Author Pubs from end of postdoc to 3-year check-in',
    '% of last author pubs from end of postdoc to 3-year check-in',
    '# of corresponding author pubs from end of postdoc to 3-year check-in',
    '% of corresponding author pubs from end of postdoc to 3-year check-in',
    'Mean Relative Citation Ratio ever up to 3-year check-in',
    'Weighted Relative Citation Ratio ever up to 3-year check-in',
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in',
    'Network Size ever up to 3-year check-in', 
    'Amount of grant funding from end of postdoc to 3-year check-in'
]

for column in numeric_columns:
    data[column] = safe_convert_to_numeric(data[column])

# Replace NaNs with median of each column
# for column in numeric_columns:
#     data[column].fillna(data[column].median(), inplace=True)

# Filter data for analytic_set = 1
filtered_data = data[data['analytic_set'] == 1]



# Check the count of non-missing values post-filtering
non_missing_counts_filtered = filtered_data.count()
print(non_missing_counts_filtered)

# Define metrics to analyze
metrics = numeric_columns  # Assuming these are the metrics to analyze

# Prepare the DataFrame for descriptive statistics
results = []

# Calculate statistics and perform statistical tests
for metric in metrics:
    group_1 = filtered_data[filtered_data['Pitt_Exit'] == 0][metric]
    group_0 = filtered_data[filtered_data['Pitt_Exit'] == 1][metric]

    # Calculate medians and quartiles
    median_1, q1_1, q3_1 = group_1.median(), group_1.quantile(0.25), group_1.quantile(0.75)
    median_0, q1_0, q3_0 = group_0.median(), group_0.quantile(0.25), group_0.quantile(0.75)

    # Perform Wilcoxon-Mann-Whitney test
    p_value = mannwhitneyu(group_1.dropna(), group_0.dropna(), alternative='two-sided').pvalue

    # Append results
    results.append({
        'Metric': metric,
        'All N=238': f"{filtered_data[metric].count()} ({filtered_data[metric].median()}), ({filtered_data[metric].quantile(0.25)}, {filtered_data[metric].quantile(0.75)})",
        'CIM=1 (Left Pitt)': f"{len(group_1)} ({group_1.median()}),({q1_1}, {q3_1})",
        'CIM=0 (Retained at Pitt)': f"{len(group_0)} ({group_0.median()}),({q1_0}, {q3_0})",
        'p-value': p_value
    })

# Convert to DataFrame
final_results_df = pd.DataFrame(results)

# Output to Excel
final_results_df.to_excel('Descriptive Statistics_Continious_Variables.xlsx', index=False)


# %%
