import pandas as pd



df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

df['ordered'] = pd.to_datetime(df['ordered'])

year_filter = df[df['ordered'].dt.year == 2017]

print(year_filter)

