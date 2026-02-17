import pandas as pd
import os
import io

df = pd.read_csv('/home/michael/NoahsRug/5784/noahs-customers.csv')

df['clean name'] =df['name'].replace(
        [' Jr.', ' Sr.',' I', ' II', ' III'], '', regex=True).str.strip()

df['last_name'] = df['clean name'].str.split().str[-1]

lastnamelist = df['last_name'].tolist()

def lets_to_nums(dictionary, letter):
    keyresult = []
    for key, value in dictionary.items():
        if letter in str(value):
            keyresult.append(key)
    if not keyresult:
        print("error")
    return keyresult

testletter = "A"
phoneword = {
        2 : "ABC",
        3 : "DEF",
        4 : "GHI",
        5 : "JKL",
        6 : "MNO",
        7 : "PQRS",
        8 : "TUV",
        9 : "WXYZ"
}

keymatch = lets_to_nums(phoneword, testletter)
print(keymatch)
print(lastnamelist)
