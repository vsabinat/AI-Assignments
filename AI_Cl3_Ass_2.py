import pandas as pd
# print word cloud

from wordcloud import WordCloud, STOPWORDS
# read the input csv file
url = "C:\\Users\\sabta\\Documents\\MTech\\AI\\"
df = pd.read_csv(url+"CommentsMarch2018.csv", encoding='latin-1')
print(df.commentBody.shape)


