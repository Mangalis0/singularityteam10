# FUNCTION 1

### START FUNCTION
def dictionary_of_metrics(items):
   
    """
    
    This function calculates the mean, median,
    variance, standard deviation, minimum and maximum of list, items, which
    contains only numerical entries.

    It return a dict with keys 'mean' , 'median' , 'std' , 'var' , 'min' , and
    'max' , corresponding to the mean, median, standard deviation, variance,
    minimum and maximum of the input list, respectively rounded to 2 decimal
    places.
    """

    # Import numpy as np to use within this function
    import numpy as np


    'Initialize dict'
    d = {}

    # Add 'mean' key to the dict with the value of the mean calculate by using
    # np.mean rounded to 2 decimal places
    d['mean'] = round(np.mean(items), 2)

    # Add 'median' key to the dict with the value of the median calculate by
    # using np.median rounded to 2 decimal places
    d['median'] = round(np.median(items), 2)

    # Add 'var' key to the dict with the value of the varience calculate by
    # using np.var rounded to 2 decimal places
    d['var'] = round(np.var(items, ddof=1), 2)

    # Add 'std' key to the dict with the value of the standard deviation
    # calculate by using np.std to 2 decimal places
    d['std'] = round(np.std(items, ddof=1), 2)

    # Add 'min' key to the dict with the value of the minimum calculate by
    # using np.min to 2 decimal places
    d['min'] = round(np.min(items), 2)

    # Add 'max' key to the dict with the value of the maximum calculate by
    # using np.max to 2 decimal places
    d['max'] = round(np.max(items), 2)

    # returns dictionary, d
    return d

### END FUNCTION

# Function 2: Five Number Summary

def five_num_summary(items):

    '''
    
    The Function Takes In A List As Integers And Returns A Dictionary Of
    A Five Number Summary.(maximum, median, minimum, first quantile, third quantile).

    Five Number Summary:
    A Set Of Descriptive Statistics That Provides Information About A Dataset.
    
    Inputs:
    The Function Takes A List, items

    Returns:
    The Function Return A Dictionary With Keys 'max', 'median', 'min', 'q1', 'q3'
    '''

    # Initialize a empty dictionary
    d = {}
    
    # Maximum value
    # Code Below Used To Calculate The Max Value Using np.max()
    # Rounded To Two Decimal Places
    d['max'] = round(np.max(items), 2)
    
    # Median calculation
    # Code Below Used To Calculate The Median Using np.median()
    # Rounded To Two Decimal Places
    d['median'] = round(np.median(items), 2)
    
    # Minimum calculation
    # Code Below Used To Calculate The Min Value Using np.min()
    # Rounded To Two Decimal Places
    d['min'] = round(np.min(items), 2)
    
    # First quantile
    # Code Below Used To Calculate The first Quantile Using np.quantile()
    # Rounded To Two Decimal Places
    d['q1'] = round(np.quantile(items, 0.25), 2)
    
    # Third quantile
    # Code Below Used To Calculate The Third Quantile Using np.quantile()
    # Rounded To Two Decimal Places
    d['q3'] = round(np.quantile(items, 0.75), 2)

    return d

### END FUNCTION

# Function 3: Date Parser

def date_parser(dates):
    """

    this function takes a list of dated timestamps (strings) 'yyyy-mm-dd hh:mm:ss' as input parameter: dates
    and returns  a list of dates (strings)
    """
    # for each element in dates, extract the first word.

    return [dt.split()[0] for dt
            in dates]

### END FUNCTION

# Function 5: Number of Tweets per Day

def number_of_tweets_per_day(df):
    """

    This function takes a dataframe of twitter data as input parameter: df
    NB input requirement: the dataframe needs to have columns for "Dates" and "Tweets" respectively
    It then returns a dataframe of the number of tweets grouped per day
    """
    # split the dated timestamp and convert the first part to a date object create a new column with the date
    # using apply method with a lambda function
    df['Date'] = df['Date'].apply(lambda dt: pd.to_datetime(dt.split()[0]))

    # group by the date
    return df.groupby('Date').count()

### END FUNCTION

# Function 6: Word Splitter


### START FUNCTION
def word_splitter(df):
    
    '''
    
    This function splits the sentences in a dataframe's column into a list of the separate words. 
    The created lists are placed in a column named 'Split Tweets' in the original dataframe. 
    This is also known as tokenization.

    Key function deliverables are:

    It takes a pandas dataframe as an input.
    The dataframe should contain a column, named 'Tweets'.
    The function splits the sentences in the 'Tweets' into a list of seperate words, and places the 
    result into a new column named 'Split Tweets'. The resulting words must all be lowercase!
    It modifies the input dataframe directly.
    
    Return:
    it returns the modified dataframe.
    '''
    
    # Creates a column, 'Split Tweets', using the .apply method of a pandas dataframe.
    # Applies the lambda function to the 'Tweets' column of the dataframe 
    # which takes the input, x, as each tweet within that column,
    # then returns lower cases of each word in a tweet, with the use of split() method.
    
    
    df['Split Tweets'] = df['Tweets'].apply(lambda x: [i.lower() for i in x.split()])
    
    return df

### END FUNCTION


# Function 7: Stop Words

def stop_words_remover(df):
    '''

    This function removes English stop words from a tweet in a Pandas Dataframe.

    Inputs:

    It takes a pandas dataframe, df, as input.
    Tokenizes the tweet by breaking the words(strings seperated by ' ') into
    string items of a list.

    It removes all stop words in the tokenised list.
    The stopwords are defined in the stop_words_dict variable defined within
    function.
    The resulting tokenised list is then placed in a column named
    "Without Stop Words" created within the DataFrame.

    Returns:
    The function returns the modified dataframe, df, which includes the column,
    "Without Stop Words".
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

    # Creates a column, "Without Stop Words", using the .apply method of a
    # pandas dataframe.
    # Applies the lambda function to the 'Tweets' column of the dataframe
    # which takes the input, x, as each tweet within that column,
    # then returns lower cases of each string in tweet as a list item,
    # provided that string is not in dict

    df['Without Stop Words'] = df['Tweets'].apply(lambda x: [word.lower()
                                                             for word in x.split()
                                                             if word.lower() not in stop_words_dict['stopwords']])

    # returns the modified dataframe
    return df

### END FUNCTION