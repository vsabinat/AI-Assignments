import pandas as pd
import numpy as np

a = ("a", "b", "c", "d", "e", "z")
#print(a[0])

b = (2, 3, 6, 8, 9, 4)
print(b[2:5])

c = list()
c.extend(a)
print(c)

c.extend(b)
print(c)

c.append(list(a))
print(c[2:5])

