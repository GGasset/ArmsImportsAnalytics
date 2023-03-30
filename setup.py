import numpy as np
import pandas as pd

global dataset_path, arms_imports, pivoted_arms_imports
dataset_path = './Arms Imports Per Country (1950-2020).csv'
arms_imports: pd.DataFrame
pivoted_arms_imports: pd.DataFrame

def main():
    global arms_imports, pivoted_arms_imports
    arms_imports = pd.read_csv(dataset_path)
    arms_imports = arms_imports.fillna(0)

    print(arms_imports.head())

    columns_to_group = []
    columns_to_group = ['Country/Region/Group'] + [v.__str__() for v in np.arange(1950, 2021, 1)]
    print(columns_to_group)
    #arms_imports.groupby()['Total']

pivoted_df = main()