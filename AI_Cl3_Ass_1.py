import pandas as pd
import seaborn as sns
# print crosstab report

# read the input csv file
url = "C:\\Users\\sabta\\Documents\\MTech\\AI\\"
df = pd.read_csv(url+"clean_automobile.csv")
print(df.columns)

# changing column names with rename()
df = df.rename(columns = {"body-style": "bodystyle",
                                  "drive-wheels":"drivewheels",
                                  "num-of-doors": "doors"})

# cross tab report between Make and Body Style columns
cross = pd.crosstab(df.make, df.bodystyle)
print(cross)

# Another cross tab
cross1 = pd.crosstab([df.make, df.doors], [df.bodystyle, df.drivewheels],
                     rownames=['Auto Comapny', 'Doors'],
                     colnames=['Body Style', 'Wheel Drive'],
                     dropna=False)

cross1h = sns.heatmap(pd.crosstab([df.make, df.doors], [df.bodystyle, df.drivewheels]),
                cmap="YlGnBu", annot=True, cbar=False)
print(cross1h)

# Group By report
grouptab = df.groupby(["make", "bodystyle"])["bodystyle"].count()
print(grouptab)
