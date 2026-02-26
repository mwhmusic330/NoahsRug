import pandas as pd



df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

customers_df = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')

def initials(full_name):
    namelist = full_name.split()
    initials = "".join([name[0].upper() for name in namelist])
    return initials

customers_df['initials'] = customers_df['name'].apply(initials)

init_find = 'JP'

init_mask = str(customers_df['initials']) == init_find

df['ordered'] = pd.to_datetime(df['ordered'])

year_filter = df[df['ordered'].dt.year == 2017]

print(year_filter)
print(init_mask)


#### Function works to get initials i tested by printing customers_df['initials'] but i am still getting all falses on comparison. Thinking a middle initial may be involved. Starting on that work around.
#### 2-26 Still looking at this tried changing the comparison string and ensuring that the output of the initials column is a string with str() method I'm just not sure why I keep getting falses? Unlss I'm reading the probem wrong theres gotta be initials 'JP' in here.
