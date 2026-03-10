import pandas as pd

pd.options.display.width = 400
pd.options.display.max_columns = 400

df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

customers_df = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')

sku_df  = pd.read_csv('/home/michael/NoahsRug/noahs-orders_items.csv')

products_df = pd.read_csv('/home/michael/NoahsRug/noahs-products.csv')

def initials(full_name):
    namelist = full_name.split()
    initials = "".join([name[0].upper() for name in namelist])
    return initials

customers_df['initials'] = customers_df['name'].apply(initials)


init_mask = customers_df['initials'] == 'JP'

init_filter = customers_df[init_mask]

df['ordered'] = pd.to_datetime(df['ordered'])

year_mask = df['ordered'].dt.year == 2017

year_filter = df[year_mask]

search_prefix = 'HOM'

clean_mask = products_df['sku'].str.startswith(search_prefix)

clean_filter = products_df[clean_mask]

items_mask = sku_df['sku'].str.startswith(search_prefix)

items_filter = sku_df[items_mask]

merge1_df  = pd.merge(init_filter, year_filter, on='customerid')
merge2_df = pd.merge(merge1_df, items_filter, on='orderid', how='inner') 
print(merge1_df)
print(items_filter)
print(merge2_df)

#### Function works to get initials i tested by printing customers_df['initials'] but i am still getting all falses on comparison. Thinking a middle initial may be involved. Starting on that work around.
#### 2-26 Still looking at this tried changing the comparison string and ensuring that the output of the initials column is a string with str() method I'm just not sure why I keep getting falses? Unlss I'm reading the probem wrong theres gotta be initials 'JP' in here.
#### update update 2-26 my comparison isnt working properly as can be seen here, tested with initials i knew existed. Now I found the real problem
#### Got it to spit out True on 'JA' so the comparison now works but 'JP' doesnt seem to exist and now im confused
### 2-27 update, simplified the mask and used 'JA' a value i know exists to check if it works and it does. I have gone back and checked my steps here multiple times now and am fairly stuck.
#### 3-9 update found the cleaning supplies, it was only one entry to look for so just have to follow the path as far as it goes now. More to come shortly.
#### 3-10 update, guess I have to cross reference for coffee and bagels too because the last merge i did should result in every row with my parameters thus far and its still a lot so more to come.
