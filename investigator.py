import pandas as pd
import os
import io

def lets_to_nums(name):
    phoneword = {
        2 : "ABCabc",
        3 : "DEFdef",
        4 : "GHIghi",
        5 : "JKLjkl",
        6 : "MNOmno",
        7 : "PQRSpqrs",
        8 : "TUVtuv",
        9 : "WXYZwxyz"
    }
    keyresult = []
    for letter in name:
        for key, value in phoneword.items():
            if letter in str(value):
                keyresult.append(key)
    if not keyresult:
        print("error")
    return str("".join(map(str, keyresult)))

full_df = pd.read_csv('/home/michael/NoahsRug/noahs-customers.csv')


full_df['clean name'] =full_df['name'].replace(
        [' Jr.', ' Sr.',' I', ' II', ' III'], '', regex=True).str.strip()

full_df['clean phone'] =full_df['phone'].replace(
        '-', '', regex=True).str.strip()

full_df['last_name'] = full_df['clean name'].str.split().str[-1]

### full_df['phone-7'] = full_df['clean phone'].astype(str).str[-7:].astype(int)

full_df['nametonum'] = full_df['last_name'].apply(lets_to_nums)

next_df = full_df[['nametonum', 'clean phone']].copy()

mask = next_df['nametonum'] == next_df['clean phone']

result  = full_df[mask]



print(result)
