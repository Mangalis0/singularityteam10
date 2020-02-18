# Power Metrics - Python Functions Using Eskom Data

**Created by Singularity (Group 10) as part of Explore Data Science Academy course requirement fulfillment.**

**The Project:** Building functions to calculate metrics using Eskom Data.

**Problem Statement:** Build python functions which calculate/analyse data from Eskom.

**Context:** Assume the role of a Data Scientist working at Eskom.

**Role Deliverables:** Build 7 functions that will process both numeric(e.g. electricity generation) and text(e.g. Tweets) data. 

## Python Topics Covered (Python knowledge tested).

1. List manipulation
2. Dictionaries
3. Basic Statistics and Aggregations
4. Function Definitions
5. PEP8 coding style
6. Git & Github



## The 7 functions

Ensure that the following packages have been imported.

```python
import numpy as np
import pandas as pd

```



# Function 1: Dictionary of Metrics

```python
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
```
# Function 2: Five Number Summary

```python
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
```

# Function 3: Date Parser

```python
def date_parser(dates):
    """

    this function takes a list of dated timestamps (strings) 'yyyy-mm-dd hh:mm:ss' as input parameter: dates
    and returns  a list of dates (strings)
    """
```

# Function 4: Municipality & Hashtag Detector

```python
def extract_municipality_hashtags(df):
    
    '''
    
    The Function Takes A Dataframe And Returns A modified Dataframe
    
    Inputs:
    The Function Takes In A Pandas Dataframe, df
    
    Returns:
    The Function Returns A Modified Dataframe
    '''
```


# Function 5: Number of Tweets per Day

```python
def number_of_tweets_per_day(df):
    """

    This function takes a dataframe of twitter data as input parameter: df
    NB input requirement: the dataframe needs to have columns for "Dates" and "Tweets" respectively
    It then returns a dataframe of the number of tweets grouped per day
    """
```

# Function 6: Word Splitter

```python
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
```
# Function 7: Stop Words

```python
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
```

## Project Continuity
This is an ongoing, live project and data may be updated from time to time.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)



