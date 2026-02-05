from pyDOE3 import bbdesign
import numpy as np
import pandas as pd

#Variable names and ranges 
component_1 = 'Protein [µM]'
component_2 = 'Succrose [mM]'
component_3 = 'Buffer [mM]'

range_component_1 = (50, 150)
range_component_2 = (200,300)
range_component_3 = (50, 150)

variation_control = (3) #Adds complimentary experiments to calculate the error

export_path = 'c:/Users/user/documents/BoxBehnken_experiment.xlsx'

# DON'T TOUCH!!
# Creating a design we can use
bbdesign = bbdesign(3, variation_control)
# Adding meaningful labels
bb_df = pd.DataFrame(bbdesign, columns=[component_1, component_2, component_3])

def scale_design(bb_df, factor_ranges):
    # Working with a copy to keep the original intact
    scaled_design = bb_df.copy()

    # Processing each factor
    for i, (low, high) in enumerate(factor_ranges):
        # Finding the middle point and the spread
        center = (high + low) / 2
        range_val = high - low

        # Converting: -1 becomes low, 0 becomes center, 1 becomes high
        scaled_design.iloc[:, i] = center + bb_df.iloc[:, i] * range_val / 2

    return scaled_design

# Setting our actual experimental ranges
factor_ranges = [
    (range_component_1),   
    (range_component_2),      
    (range_component_3),
]
# Transforming to real values
scaled_df = scale_design(bb_df, factor_ranges)

# Printing the results to an Excel for use in the Lab
scaled_df.index += 1
scaled_df.index.name = 'Run'
scaled_df['Freezetime'] = ''
scaled_df['Thawtime'] = ''
scaled_df.to_excel(export_path)
# Controll for the output in the console
print(scaled_df)
