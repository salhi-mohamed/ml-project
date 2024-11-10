import numpy as np
import pandas as pd
medical_df = pd.read_csv('https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv')
print(medical_df)
medical_df.info()