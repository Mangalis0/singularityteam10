# import the powermetrics module created with the alias pwm
from powermetrics import powermetrics as pwm

# Import pandas and numpy
import pandas as pd
import numpy as np

# END OF MODULE IMPORT

# START DATA IMPORT
# Import Electrification by province (EBP) data
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:, 1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',', '').astype(int)

# Import Twitter data
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)

# Important Variables
# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {'@CityofCTAlerts': 'Cape Town',
            '@CityPowerJhb': 'Johannesburg',
            '@eThekwiniM': 'eThekwini',
            '@EMMInfo': 'Ekurhuleni',
            '@centlecutility': 'Mangaung',
            '@NMBmunicipality': 'Nelson Mandela Bay',
            '@CityTshwane': 'Tshwane'}

# dictionary of english stopwords
stop_words_dict = {'stopwords': ['where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
                                 'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
                                 'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
                                 'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
                                 'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
                                 'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
                                 'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
                                 'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
                                 'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
                                 'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
                                 'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
                                 'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
                                 'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
                                 'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
                                 'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
                                 'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
                                 'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
                                 'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
                                 "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
                                 'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
                                 'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
                                 'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
                                 'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
                                 'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
                                 'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
                                 'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
                                 'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
                                 'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
                                 'same', 'were', 'it', 'every', 'third', 'together'
                                 ]
                   }

# END OF DATA IMPORT


# Test Function 1: dictionary_of_metrics
def test_dictionary_of_metrics():

    """"
    Make sure dictionary_of_metrics works correctly
    """

    assert pwm.dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                                  'median': 24403.5,
                                                  'var': 108160153.17,
                                                  'std': 10400.01,
                                                  'min': 8842.0,
                                                  'max': 39660.0
                                                  }, 'Incorrect'

# END OF Test Function 1


# Test Function 2: five_num_summary
def test_five_num_summary():

    """"
    Make sure five_num_summary works correctly
    """

    assert pwm.five_num_summary(gauteng) == {'max': 39660.0,
                                             'median': 24403.5,
                                             'min': 8842.0,
                                             'q1': 18653.0,
                                             'q3': 36372.0
                                             }, 'Incorrect'

# END OF Test Function 2


# Test function 3: date_parser
def test_date_parser():

    """"
    Make sure date_parser works correctly
    """
    assert pwm.date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'Incorrect'
    assert pwm.date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20'], 'Incorrect'

# END OF Test Function 3


# Test function 4: extract_municipality_hashtags
def test_extract_municipality_hashtags():

    """"
    Make sure extract_municipality_hashtags works correctly
    """

    assert pwm.extract_municipality_hashtags(twitter_df.copy()).shape == (200, 4), 'Incorrect'  # test size of dataframe
    assert 'Tweets' in pwm.extract_municipality_hashtags(twitter_df.copy())\
           and 'Date' in pwm.extract_municipality_hashtags(twitter_df.copy())\
           and 'municipality' in pwm.extract_municipality_hashtags(twitter_df.copy())\
           and 'hashtags' in pwm.extract_municipality_hashtags(twitter_df.copy()), 'Incorrect'

# END OF Test Function 4


# Test function 5: number_of_tweets_per_day
def test_number_of_tweets_per_day():

    """"
    Make sure number_of_tweets_per_day works correctly
    """

    assert pwm.number_of_tweets_per_day(twitter_df.copy()).shape == (10, 1), 'Incorrect'
    assert 'Tweets' in pwm.number_of_tweets_per_day(twitter_df.copy()), 'Incorrect'

# END OF Test Function 5


# Test function 6: word_splitter
def test_word_splitter():

    """"
    Make sure word_splitter works correctly
    """

    assert pwm.word_splitter(twitter_df.copy()).shape == (200, 3), 'Incorrect'
    assert 'Tweets' in pwm.word_splitter(twitter_df.copy())\
           and 'Date' in pwm.word_splitter(twitter_df.copy())\
           and 'Split Tweets' in pwm.word_splitter(twitter_df.copy()), 'Incorrect'

# END OF Test Function 6


# Test function 7: stop_words_remover
def test_stop_words_remover():

    """"
    Make sure stop_words_remover works correctly
    """
    assert pwm.stop_words_remover(twitter_df.copy()).shape == (200, 3), 'Incorrect'
    assert 'Tweets' in pwm.stop_words_remover(twitter_df.copy())\
           and 'Date' in pwm.stop_words_remover(twitter_df.copy())\
           and 'Without Stop Words' in pwm.stop_words_remover(twitter_df.copy()), 'Incorrect'