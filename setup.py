
import os
import numpy as np
import pandas as pd

dataset_path = './Arms Imports Per Country (1950-2020).csv'
cleaned_dataset_path = './ArmsImport.csv'
original_arms_imports: pd.DataFrame
arms_imports: pd.DataFrame
original_arms_imports = pd.read_csv(dataset_path)
original_arms_imports.fillna(0, inplace=True)

def main():
    if os.path.isfile(cleaned_dataset_path) and __name__ != '__main__':
        arms_imports = pd.read_csv(cleaned_dataset_path)
        return 0

    print(original_arms_imports.head())
    organization_year_data = [year.__str__() for year in np.arange(1950, 2021, 1)] + ['Total']

    year_data = organization_year_data * len(original_arms_imports['Country/Region/Group'])
    organization_data: list[str]
    organization_data = []
    for organization in original_arms_imports['Country/Region/Group']:
        organization_data += [organization] * len(organization_year_data)
    values: list[float]
    values = []
    for organization in original_arms_imports['Country/Region/Group']:
        organization_condition = original_arms_imports['Country/Region/Group'] == organization
        organization_values = original_arms_imports[organization_condition][organization_year_data]
        organization_values: pd.DataFrame
        organization_values = list(organization_values.values[0])

        values += organization_values
        print(f'{len(values)}/{len(year_data)}')
    df_data = {
        'Country/Region/Group': organization_data,
        'year': year_data,
        'value': values
        }

    arms_imports = pd.DataFrame(data=df_data)
    print(arms_imports.head())
    arms_imports.to_csv(cleaned_dataset_path)

    return 0

main()