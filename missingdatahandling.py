import pandas as pd
import numpy as np

# Data
data = {'Name': ['Anunay', 'Bandar', 'Chamgadar', 'Davidputra'],
        'Age': [25, np.nan, 30, 22],
        'Score': [85, 90, np.nan, np.nan]}
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull().sum())
