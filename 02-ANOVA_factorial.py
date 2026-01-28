import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_excel('C:/Users/GAURIJU1/OneDrive - Novartis Pharma AG/Documents/fractional_experiment_dummy.xlsx')

# CONVERT THE EXCEL TO DATAFRAME
df = pd.DataFrame(data)
#print(df)

# SCALE THE DATA SO THE EFFECTS ARE INDEPENDENT OF UNITS/SCALE
scaled_data = df.apply(lambda x: (x - np.mean(x)) / np.std(x) 
                       if x.name != 'Run' and x.name != 'Freezetime' and x.name != 'Thawtime'
                       else x)
#print(scaled_data)

# MODEL OF EFFECTS AND ANOVA OF THEM FOR FREEZING
freeze_model = ols('Freezetime ~ C(Protein) + C(Succrose) + C(Histidine) + C(Arginine) + C(Methionine) + C(PLX188)', data=scaled_data).fit()
freeze_anova_table = sm.stats.anova_lm(freeze_model, typ=2)
#print(freeze_anova_table)

# MODEL OF EFFECTS AND ANOVA OF THEM FOR THAWING
thaw_model = ols('Thawtime ~ C(Protein) + C(Succrose) + C(Histidine) + C(Arginine) + C(Methionine) + C(PLX188)', data=scaled_data).fit()
thaw_anova_table = sm.stats.anova_lm(thaw_model, typ=2)
#print(thaw_anova_table)

# CONVERTING AND EXPORTING THE ANOVA TABLES WITH THE BACKGROUND DATA
freeze_data = pd.DataFrame(freeze_anova_table)
thaw_data = pd.DataFrame(thaw_anova_table)
with pd.ExcelWriter('C:/Users/GAURIJU1/OneDrive - Novartis Pharma AG/Documents/ANOVA_fractional_dummy.xlsx') as writer:
    freeze_data.to_excel(writer, sheet_name='ANOVA Freeze')
    thaw_data.to_excel(writer, sheet_name='ANOVA Thaw')
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    scaled_data.to_excel(writer,sheet_name='Normalised Data', index=False)
