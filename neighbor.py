import pandas as pd

pd.options.display.width = 400
pd.options.display.max_columns = 400

df = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')

df['birthdate'] = pd.to_datetime(df['birthdate'])

location = 'Jamaica, NY' 

location_mask = df['citystatezip'].str.startswith(location)

year_mask = df['birthdate'].dt.year.isin([1963, 1975, 1987, 1999, 2011, 2023])

month_day_mask = ((df['birthdate'].dt.month == 6) & (df['birthdate'].dt.day >= 21) |
                  (df['birthdate'].dt.month == 7) & (df['birthdate'].dt.day <= 22))  

filter = df[year_mask & month_day_mask & location_mask]

print(filter)
