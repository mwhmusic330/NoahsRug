import pandas as pd



df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

customers_df = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')

def initials(name):
    return ''.join(word[0] for word in name.split()).upper()

customers_df['initials'] = customers_df['name'].apply(initials)

init_find = 'JP'

init_mask = customers_df['initials'] == init_find

df['ordered'] = pd.to_datetime(df['ordered'])

year_filter = df[df['ordered'].dt.year == 2017]

print(year_filter)
print(init_mask)

