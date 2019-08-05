import pandas as pd

# read csv file
url = "C:/Users/sabta/Documents/MTech/AI/"
data = pd.read_csv(url+"winemag-data_100.csv", delimiter=',')
# find datatypes of columns and put into a dataframe
# 0 column of new DF contains names of columns read from CSV
dcols = pd.DataFrame()
dcols['cnames'] = data.columns.values
dcoltypes = list(data.dtypes)

# 1 column of DF contains datatypes of these columns
dcols['datypes'] = dcoltypes

# 2 column of DF contains new column names
dcols['ncols'] = ""

i = 0
for i in range(0, len(dcols)):
    dcols.at[i,'ncols'] = "count_" + str(dcols.at[i,'cnames'])

# a df made for only object columns
colist = pd.DataFrame(dcols[dcols['datypes'] == 'object'])

# a df made for only int columns
intlist = pd.DataFrame(dcols[dcols['datypes'] == 'int64'])

count = 0
# add 2 columns in main DF data for storing counts of words for every row
while count < 2:
    pos = data.columns.get_loc(colist.iloc[count,0])    # get position of column in main DF data
    data[colist.iloc[count,2]] = colist.iloc[count,2]   # in the main DF data, add a column with the name count_cn
    count = count + 1

count = 0
# add columns for int values in main DF for storing means of int columns
while count in range(0, len(intlist)):
    pos = data.columns.get_loc(intlist.iloc[count,0])
    data[intlist.iloc[count,2]] = intlist.iloc[count,2]
    data[intlist.iloc[count,2]] = None
    count = count + 1

count = 0
# update values in the main DF data with word counts for every row
while count < 2:
    sourcecol = colist.iloc[count,0]
    targetcol = colist.iloc[count,2]
    data[targetcol] = data[sourcecol].str.split().map(len)
    count = count + 1

count = 0
# update values in the main DF data with mean value for the column
while count < 2:
    sourcecol = intlist.iloc[count,0]
    targetcol = intlist.iloc[count,2]
    data[targetcol] = data[sourcecol].mean()
    count = count + 1

data.to_csv(url+"Sabina_AI_Cl1_output.csv")


