import pandas as pd

pd.options.display.width = 400
pd.options.display.max_columns = 400

df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

df_products = pd.read_csv('/home/michael/NoahsRug/noahs-products.csv')

sku_df  = pd.read_csv('/home/michael/NoahsRug/noahs-orders_items.csv')

cus_df  = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')

location = "Staten Island, NY"

location_mask = cus_df['citystatezip'].str.startswith(location)

location_filter = cus_df[location_mask]

search_prefix = 'COL'

sku_mask = df_products['sku'].str.contains(search_prefix)
sku_filter = df_products[sku_mask]

desc_mask = sku_filter['desc'].str.contains('Jersey')
desc_filter = sku_filter[desc_mask]


print(desc_filter)

