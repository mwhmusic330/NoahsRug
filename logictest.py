name  = "Michael"
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
my_name = lets_to_nums(name)
print(my_name)
