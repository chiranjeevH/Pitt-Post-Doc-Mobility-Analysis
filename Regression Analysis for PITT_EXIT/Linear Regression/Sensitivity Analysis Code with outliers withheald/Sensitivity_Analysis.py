

#%%
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot



# Load your merged dataset
data = pd.read_excel('datasetname.xlsx')

# Filter the data where analytic_set = 1
data = data[data['analytic_set'] == 1]

# Label encode categorical variables
data['Gender'] = data['Gender'].astype('category').cat.codes
data['URM'] = data['URM'].astype('category').cat.codes
data['FIS_Nationality'] = data['FIS_Nationality'].astype('category').cat.codes

# Impute missing values for the entire DataFrame
imputer = SimpleImputer(strategy='most_frequent')
data[:] = imputer.fit_transform(data)

# Ensure all data is numeric (optional based on your dataset specifics)
data = data.apply(pd.to_numeric, errors='coerce')

# Impute any remaining missing values after conversion
data.fillna(data.mean(), inplace=True)








model_results = []
outcome_variables = [
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
    'Network Size ever up to 3-year check-in'
]
# Define the constant baseline covariates
baseline_covariates = [
    '# of Pubs ever to end of postdoc',
    'H-Index ever to end of postdoc',
    'Cat. Normal Citation Impact ever to End of Postdoc',
    '# of 1st Author Pubs ever to end of postdoc',
    '% of 1st Author Pubs ever to end of postdoc',
    '# of last Author Pubs ever to end of postdoc',
    '% of last author pubs ever to end of postdoc',
    '# of corresponding author pubs ever to end of postdoc',
    '% of corresponding author pubs ever to end of postdoc',
    'Mean Relative Citation Ratio ever to end of postdoc',
    'Weighted Relative Citation Ratio ever to end of postdoc',
    '# of Pubs without Postdoc Mentor during the postdoc',
    'Network Size ever to end of postdoc'
    
]

baseline_covariate_mapping = {
    '# of Pubs from end of postdoc to 3-year check-in': '# of Pubs ever to end of postdoc',
    'H-Index ever up to 3 year check-in': 'H-Index ever to end of postdoc',
    'Cat. Normal Citation Impact ever up to 3-year check-in': 'Cat. Normal Citation Impact ever to End of Postdoc',
    '# of 1st Author Pubs from end of postdoc to 3-year check-in': '# of 1st Author Pubs ever to end of postdoc',
    '% of 1st Author Pubs from end of postdoc to 3-year check-in': '% of 1st Author Pubs ever to end of postdoc',
    '# of last Author Pubs from end of postdoc to 3-year check-in': '# of last Author Pubs ever to end of postdoc',
    '% of last author pubs from end of postdoc to 3-year check-in': '% of last author pubs ever to end of postdoc',
    '# of corresponding author pubs from end of postdoc to 3-year check-in': '# of corresponding author pubs ever to end of postdoc',
    '% of corresponding author pubs from end of postdoc to 3-year check-in': '% of corresponding author pubs ever to end of postdoc',
    'Mean Relative Citation Ratio ever up to 3-year check-in': 'Mean Relative Citation Ratio ever to end of postdoc',
    'Weighted Relative Citation Ratio ever up to 3-year check-in': 'Weighted Relative Citation Ratio ever to end of postdoc',
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in': '# of Pubs without Postdoc Mentor during the postdoc',
    'Network Size ever up to 3-year check-in': 'Network Size ever to end of postdoc'
}



# Create a list of models and their respective covariates
models = [
    {
        'name': 'Model 1',
        'additional_covariates': []
    },
    {
        'name': 'Model 2',
        'additional_covariates': ['Gender', 'URM']
    },
    {
        'name': 'Model 3',
        'additional_covariates': ['Gender', 'URM', 'FIS_Nationality', 'Months_Worked_in_appointment']
    }
]




def extract_model_summary(refined_model, covariate_name):
    coef = refined_model.params[covariate_name]
    ci_lower, ci_upper = refined_model.conf_int().loc[covariate_name]
    p_value = refined_model.pvalues[covariate_name]
    summary = {
        'Variable': covariate_name,  # This will hold the name of the covariate
        'Coefficient': coef,
        '95% CI Lower': ci_lower,
        '95% CI Upper': ci_upper,
        'P-value': p_value
    }
    return summary


def identify_influential_points(model):
    influence = model.get_influence()
    cooks_d = influence.cooks_distance[0]
    threshold = 4 / len(cooks_d)
    influential_points = np.where(cooks_d > threshold)[0]  # This should correctly identify indices
    return influential_points



#Diagnostic Plots to Identify Outliers
# def diagnostic_plots(refined_model, X_refined, y_refined, model_name, outcome_var):
#     """
#     Generates and shows diagnostic plots for a linear regression model.
#     """
#     fig, ax = plt.subplots(2, 2, figsize=(15, 12))
#     sm.graphics.plot_fit(refined_model, 0, ax=ax[0, 0])
#     ax[0, 0].set_title(f'Residuals vs Fitted for {outcome_var}')
#     sm.qqplot(refined_model.resid, line='s', ax=ax[0, 1])
#     ax[0, 1].set_title(f'Normal Q-Q for {outcome_var}')
#     standardized_residuals = refined_model.get_influence().resid_studentized_internal
#     ax[1, 0].scatter(refined_model.fittedvalues, np.sqrt(np.abs(standardized_residuals)), alpha=0.5)
#     ax[1, 0].set_xlabel('Fitted values')
#     ax[1, 0].set_ylabel('Sqrt of Standardized Residuals')
#     ax[1, 0].set_title(f'Scale-Location for {outcome_var}')
#     sm.graphics.influence_plot(refined_model, ax=ax[1, 1], criterion="cooks")
#     ax[1, 1].set_title(f'Influence Plot for {outcome_var}')
#     plt.tight_layout()
#     plt.show()


from scipy import stats

# Adjusted workflow to include fitting models with specified covariates and their respective baseline covariate
with pd.ExcelWriter('Sensitivity_Analysis_Result.xlsx') as writer:
    for model_info in models:
        model_name = model_info['name']
        additional_covariates = model_info['additional_covariates']
        all_model_results = []
        
        for outcome_var in outcome_variables:
            baseline_covariate = baseline_covariate_mapping[outcome_var]
            covariates = ['Pitt_Exit'] + [baseline_covariate] + additional_covariates  
            
            X = data[covariates]
            y = data[outcome_var]
            
            # Standardize X and y
            X_standardized = pd.DataFrame(stats.zscore(X), columns=X.columns)
            y_standardized = pd.Series(stats.zscore(y), name=y.name)

            # Add a constant to the standardized predictors
            X_with_const = sm.add_constant(X_standardized)
            
            # Fit the initial model with standardized predictors and outcome
            initial_model = sm.OLS(y_standardized, X_with_const).fit()
            print(f"Initial Model Summary for {model_name} - {outcome_var}:")
            print(initial_model.summary())
            
            
            # Identifying influential points
            influential_points = identify_influential_points(initial_model)

            # Refitting the model without influential points
            X_refined = X_with_const.loc[~X_with_const.index.isin(influential_points)]
            y_refined = y_standardized.loc[~y_standardized.index.isin(influential_points)]
            refined_model = sm.OLS(y_refined, X_refined).fit()
            
            print("\n")
            print(f"Refined Model Summary for {model_name} - {outcome_var}:")
            print(refined_model.summary())
            
            # To call Diagnostic Plots Function
            # diagnostic_plots(refined_model, X_refined, y_refined, model_name, outcome_var)

            # Extract model summaries
            for covariate_name in X_with_const.columns:
                if covariate_name == 'const':
                    continue
                summary = extract_model_summary(refined_model, covariate_name)
                summary['Outcome Variable'] = outcome_var
                model_results.append(summary)
        
        # Write to Excel
        model_results_df = pd.DataFrame(model_results)
        model_results_df.to_excel(writer, sheet_name=model_name, index=False)