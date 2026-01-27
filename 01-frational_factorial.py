from pyDOE3 import fracfact, fracfact_opt, fracfact_by_res
import numpy as np
import pandas as pd
# Variable names and ranges

component_1 = "Protein"
component_2 = "Succrose"
component_3 = "Histamin"
component_4 = "PEG400"
component_5 = "PS20"

range_component_1 = (-1, 1)
range_component_2 = (-1, 1)
range_component_3 = (-1, 1)
range_component_4 = (-1, 1)
range_component_5 = (-1, 1)

export_path = 'c:/Users/GAURIJU1/OneDrive - Novartis Pharma AG/Documents/fractional_experiment.xlsx'


# 1. DEFINE EXPERIMENT PARAMETERS
factors = {
    component_1: range_component_1,
    component_2: range_component_2, 
    component_3: range_component_3,
    component_4: range_component_4,
    component_5: range_component_5
}

num_factors = 5
num_generators = 2

# 2. FIND OPTIMAL DESIGN
optimal_generator, aliases, cost = fracfact_opt(num_factors, num_generators)
print(f"Optimal generator: {optimal_generator}")

# 3. CREATE DESIGN
design = fracfact(optimal_generator)

# 4. CONVERT TO DATAFRAME
df = pd.DataFrame(design, columns=factors.keys())

# 5. MAP TO REAL VALUES
for factor, (low, high) in factors.items():
    df[factor] = df[factor].map({-1: low, 1: high})

# 6. RANDOMIZE AND EXPORT
df.index += 1
df.index.name = 'Run'
df['Freezetime'] = ''
df['Thawtime'] = ''
df.to_excel(export_path)
print(df)
