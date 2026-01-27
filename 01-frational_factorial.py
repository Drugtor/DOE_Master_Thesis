from pyDOE3 import fracfact, fracfact_opt, fracfact_by_res
import numpy as np
import pandas as pd
# Variable names and ranges

component_1 = "Protein[mg/ml]"
component_2 = "Succrose[mM]"
component_3 = "Histidine[mM]"
component_4 = "Arginine[mM]"
component_5 = 'Methionine[mM]'
component_6 = 'PLX188[%]'

range_component_1 = (0, 100)
range_component_2 = (0, 160)
range_component_3 = (0, 20)
range_component_4 = (0, 50)
range_component_5 = (0, 5)
range_component_6 = (0, 0.1)

export_path = 'c:/Users/GAURIJU1/OneDrive - Novartis Pharma AG/Documents/fractional_experiment_v3.xlsx'


# 1. DEFINE EXPERIMENT PARAMETERS
factors = {
    component_1: range_component_1,
    component_2: range_component_2, 
    component_3: range_component_3,
    component_4: range_component_4,
    component_5: range_component_5,
    component_6: range_component_6,
}

num_factors = 6
num_generators = 3

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
