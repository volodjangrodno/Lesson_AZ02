import pandas as pd
import numpy as np

dates = pd.date_range('2013-01-28', periods=10, freq='D')
values = np.random.randn(10)

df = pd.DataFrame({'date': dates, 'value': values})
df.set_index('date', inplace=True)

print(df)

mount = df.resample('M').mean()

print(mount)