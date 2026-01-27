import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_excel('C:/Users/GAURIJU1/OneDrive - Novartis Pharma AG/Documents/fractional_experiment.xlsx')

df = pd.DataFrame(data)

freeze_model = ols('Freezetime ~ C(Protein) + C(Succrose) + C(Histamin) + C(PEG400) + C(Arginin) + C(Methionin)', data=df).fit()
freeze_anova_table = sm.stats.anova_lm(freeze_model, typ=2)
print(freeze_anova_table)

thaw_model = ols('Thawtime ~ C(Protein) + C(Succrose) + C(Histamin) + C(PEG400) + C(Arginin) + C(Methionin)', data=df).fit()
thaw_anova_table = sm.stats.anova_lm(thaw_model, typ=2)
print(thaw_anova_table)

freeze_data = pd.DataFrame(freeze_anova_table)
thaw_data = pd.DataFrame(thaw_anova_table)
with pd.ExcelWriter('C:/Users/GAURIJU1/OneDrive - Novartis Pharma AG/Documents/ANOVA_fractional.xlsx') as writer:
    freeze_data.to_excel(writer, sheet_name='Freeze')
    thaw_data.to_excel(writer, sheet_name='Thaw')
