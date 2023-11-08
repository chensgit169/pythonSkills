import pandas as pd
import numpy as np

array = np.linspace(0, 1, 10000).reshape(100, 100)
array[array < 0.5] = None
df = pd.DataFrame(array)
df.to_excel('excel1.xlsx', sheet_name='Sheet1', index=True)
