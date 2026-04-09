import pandas as pd

pd.options.display.width = 400
pd.options.display.max_columns = 400

df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

df_products = pd.read_csv('/home/michael/NoahsRug/noahs-products.csv')

sku_df  = pd.read_csv('/home/michael/NoahsRug/noahs-orders_items.csv')

cus_df  = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')


df['ordered'] = pd.to_datetime(df['ordered'])
df['shipped'] = pd.to_datetime(df['shipped'])


time_mask = df['shipped'].dt.hour == 4


time_filter = df[time_mask]

merge1_df = pd.merge(time_filter, sku_df, on='orderid')

bky_mask = merge1_df['sku'].str.startswith('BKY')

merge2_df = pd.merge(merge1_df[bky_mask], df_products, on='sku')

merge3_df = pd.merge(merge2_df, cus_df, on='customerid')



columns = ["orderid", "customerid", "shipped", "items", "sku", "qty", "desc", "wholesale_cost", "name", "address", "citystatezip", "phone"]





print(merge3_df[columns])
