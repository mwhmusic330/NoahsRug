import pandas as pd

pd.options.display.width = 400
pd.options.display.max_columns = 400

df = pd.read_csv('/home/michael/NoahsRug/noahs-orders.csv')

df_products = pd.read_csv('/home/michael/NoahsRug/noahs-products.csv')

sku_df  = pd.read_csv('/home/michael/NoahsRug/noahs-orders_items.csv')

cus_df  = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')