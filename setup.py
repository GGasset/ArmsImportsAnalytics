import os
import math
import numpy as np
import pandas as pd

countries_path = './countries of the world.csv'
cleaned_countries_path = './countries.data'
arms_import_path = './Arms Imports Per Country (1950-2020).csv'
cleaned_arms_import_path = './ArmsImport.data'

def clean_dfs():
    clean_arms_dataframe()
    clean_countries_dataframe()
    return 0

def clean_arms_dataframe():
    original_arms_imports = pd.read_csv(arms_import_path)
    original_arms_imports.fillna(0, inplace=True)
    print(original_arms_imports.head())
    organization_year_data = [year.__str__() for year in np.arange(1950, 2021, 1)]

    year_data = organization_year_data * len(original_arms_imports['Country/Region/Group'])
    organization_data: list[str]
    organization_data = []
    for organization in original_arms_imports['Country/Region/Group']:
        organization_data += [organization] * len(organization_year_data)
    values: list[int]
    values = []

    total_imports: list[int]
    total_imports = []
    for organization in original_arms_imports['Country/Region/Group']:
        organization_condition = original_arms_imports['Country/Region/Group'] == organization
        arms_imports_of_organization = original_arms_imports[organization_condition]
        organization_values = arms_imports_of_organization[organization_year_data]
        organization_values: pd.DataFrame
        organization_values = list(organization_values.values[0])

        values += organization_values
        total_imports += [arms_imports_of_organization[['Total']].iloc[0, 0]] * len(organization_values)
        print(f'{len(values)}/{len(year_data)}')

    df_data = {
        'country': organization_data,
        'year': year_data,
        'value': values,
        'total_imports': np.array(total_imports, dtype='float32')
        }

    arms_imports = pd.DataFrame(data=df_data)
    print(arms_imports.drop_duplicates(subset='country').head())
    arms_imports.to_feather(cleaned_arms_import_path)
    print('Arms imports dataset cleaned and saved.')
    return arms_imports

def clean_countries_dataframe():
    countries = pd.read_csv(countries_path)
    print("'" + countries.iloc[0, 0] + "'")

    countries_col = list(countries['Country'].values)
    countries_col: list[str]
    cleaned_countries_col = [country.removesuffix(' ') for country in countries_col]
    countries['Country'] = cleaned_countries_col
    countries['categorized_GDP'] = countries['GDP ($ per capita)'].apply(categorizeGDP)
    print("'" + countries.iloc[0, 0] + "'")
    countries.reset_index(inplace=True, drop=True)
    print(countries.head())
    countries.to_feather(cleaned_countries_path)
    print('Countries dataframe cleaned and saved')
    return 0

def categorizeGDP(gdp: float) -> str:
    if math.isnan(gdp):
        return np.nan

    if gdp in range(15000):
        return 'low GDP'
    
    if gdp in range(27000):
        return 'medium GDP'
    
    if gdp in range(10 ** 6):
        return 'high GDP'
    
    return 'negative GDP'

if __name__ == '__main__':
    clean_dfs()