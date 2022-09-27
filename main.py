import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
from cleantext import clean


# Create list to add tweet data to
tweets_list1 = []

# scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:@kabalanhady').get_items()):
    if i > 100:
        break
    temp = re.sub("@[A-Za-z0-9_]+", "", tweet.content)  # remove mentions
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)  # remove hashtags
    temp = re.sub(r"http\S+", "", temp)  # remove links starting with https
    temp = re.sub(r"www.\S+", "", temp)  # remove links starting with www
    temp = re.sub('[()/!?؟:;.,]', ' ', temp)  # remove punctuations
    temp = re.sub('\[.*?\]', ' ', temp)  # remove punctuations
    temp = re.sub('"', " ", temp)  # remove single quotes
    temp = re.sub("'", " ", temp)  # remove double quotes
    temp = re.sub("[a-zA-Z]", "", temp)  # remove all english letters
    # temp = clean(temp, no_emoji=True)  # remove emojis
    tweets_list1.append([temp, tweet.user.username, tweet.hashtags])

# Create dataframe from list of tweets
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Text', 'Username', 'Hashtags'])
file_name = 'Tweets2cleanedfinal.xlsx'
tweets_df1.to_excel(file_name)
print('DataFrame to Excel File sucessfull!')
