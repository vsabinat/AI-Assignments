import numpy as np
import pandas as pd
import itertools as it

# df = pd.read_csv("/Users/sabinatandon/Documents/MTech/AI/nba.csv")
df = pd.read_csv("/Users/sabinatandon/Documents/MTech/AI/gapminder.csv")

df.head()

a = np.array([[1,7,3,4],[3,2,4,1]])
print(a)

# Ravel Numpy
print(a.ravel())

# Flatten Numpy Array - creates a new array
print(a.flatten())

res = df.corr()

print(res)
print(res.iloc[1,2])

get_comb = list(it.product(res,res))
print(res.loc[get_comb[1]])

# Column list on axis 0.
firtup = []
sectup = []
thitup = []
fortup = []

# def findxy():
for i in range(0, len(get_comb)):
    val = res.loc[get_comb[i]]
    val = np.abs(val)
    print(val)

    if val <= 0.20:
        firtup.append(get_comb[i])
    elif val > 0.20 and val <= 0.6:
        sectup.append(get_comb[i])
    elif val > 0.6 and val <= 0.8:
        thitup.append(get_comb[i])
    else:
        fortup.append(get_comb[i])

mybuck = ["0.2", "0.6", "0.8", "1.0"]

resdf = pd.DataFrame(list(zip(firtup, sectup, thitup, fortup)), columns=mybuck)

print(resdf.head())


