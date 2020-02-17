# Function 3: Date Parser

def date_parser(dates):
    """

    this function takes a list of dated timestamps (strings) 'yyyy-mm-dd hh:mm:ss' as input parameter: dates
    and returns  a list of dates (strings)
    """

    return

# Function 5: Number of Tweets per Day

def number_of_tweets_per_day(df):
    """

    This function takes a dataframe of twitter data as input parameter: df
    NB input requirement: the dataframe needs to have columns for "Dates" and "Tweets" respectively
    It then returns a dataframe of the number of tweets grouped per day
    """

# Function 7: Stop Words

def stop_words_remover(df):
    '''

    This function removes English stop words from a tweet in a Pandas Dataframe.

    Inputs:

    It takes a pandas dataframe, df, as input.
    Tokenizes the tweet by breaking the words(strings seperated by ' ') into string items of a list.

    It removes all stop words in the tokenised list.
    The stopwords are defined in the stop_words_dict variable defined within function.
    The resulting tokenised list is then placed in a column named "Without Stop Words" 
    created within the DataFrame.

    Returns:
    The function returns the modified dataframe, df, which includes the column, "Without Stop Words".
    '''

    stop_words_dict = {
        'stopwords': [
            'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
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

    # Creates a column, "Without Stop Words", using the .apply method of a pandas dataframe.
    # Applies the lambda function to the 'Tweets' column of the dataframe 
    # which takes the input, x, as each tweet within that column,
    # then returns lower cases of each string in tweet as a list item,
    # provided that string is not in dict

    df['Without Stop Words'] = df['Tweets'].apply(lambda x: [word.lower()
                                                             for word in x.split()
                                                             if word.lower() not in stop_words_dict['stopwords']])

    # returns the modified dataframe
    return df
