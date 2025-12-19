import pandas as pd
import numpy as np

df=pd.read_csv("sample_sales.csv")

df['revenue']=df['quantity']*df['unit_price']

df['category_upper']=df['category'].map(lambda x: x.upper())

df_filtered=df[df['revenue']>50]

summary=df.groupby('category')['revenue'].sum().reset_index()

summary.to_csv("summary_output.csv", index=False)
print("Done:", summary)
