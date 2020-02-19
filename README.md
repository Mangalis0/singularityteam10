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



## Installation and Usage

Ensure that the following packages have been installed and imported.

```bash
pip install numpy
pip install pandas
```

#To Install Power Metrics(The 7 Functions)

```bash
pip install git+https://github.com/Mangalis0/singularityteam10.git
```

#To Upgrade Power Metrics(The 7 Functions)

```bash
pip install --upgrade git+https://github.com/Mangalis0/singularityteam10.git
```

#To access/use the functions
```python
from powermetrics import powermetrics as pm

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

#Expample Output
dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}

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

#Expample Output
five_num_summary(gauteng) == {
    'max': 39660.0,
    'median': 24403.5,
    'min': 8842.0,
    'q1': 18653.0,
    'q3': 36372.0
}

```



# Function 3: Date Parser

```python
def date_parser(dates):
    """

    this function takes a list of dated timestamps (strings) 'yyyy-mm-dd hh:mm:ss' as input parameter: dates
    and returns  a list of dates (strings)
    """
#Expample Output
date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']

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
#Example Output
| Tweets | Date | Municiplity | Hashtags |
| ------------- |:-------------:| -----:| -----: |
| 0	@BongaDlulane Please send an email to mediades | 2019-11-29 12:50:54 | Nan | Nan |
| 1	@saucy_mamiie Pls log a call on 0860037566 | 2019-11-29 12:46:53 | Nan | Nan |
| 2	@BongaDlulane Query escalated to media desk. | 2019-11-29 12:46:10 | Nan | Nan |


# Function 5: Number of Tweets per Day

```python
def number_of_tweets_per_day(df):
    """

    This function takes a dataframe of twitter data as input parameter: df
    NB input requirement: the dataframe needs to have columns for "Dates" and "Tweets" respectively
    It then returns a dataframe of the number of tweets grouped per day
    """
```

#Example Output
| Date | Tweets | 
| ------------- |:-------------:| 
| 2019-11-20 | 18 | 
| 2019-11-21 | 11 | 
| 2019-11-22 | 25 |


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
#Example Output
| Tweets | Date | Split Tweets | 
| ------------- |:-------------:| -----:|
| 0	@BongaDlulane Please send an email to mediades | 2019-11-29 12:50:54 | [@bongadlulane, please, send, an, email, to, m... |
| 1	@saucy_mamiie Pls log a call on 0860037566 | 2019-11-29 12:46:53 | [@saucy_mamiie, pls, log, a, call, on, 0860037.. | 
| 2	@BongaDlulane Query escalated to media desk. | 2019-11-29 12:46:10 | [@bongadlulane, query, escalated, to, media, d. |


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
| Tweets | Date | Without Stop Words | 
| ------------- |:-------------:| -----:|
| 0	@BongaDlulane Please send an email to mediades | 2019-11-29 12:50:54 | [@bongadlulane, send, email, mediadesk@eskom.c.. |
| 1	@saucy_mamiie Pls log a call on 0860037566 | 2019-11-29 12:46:53 | [@saucy_mamiie, pls, log, 0860037566] | 
| 2	@BongaDlulane Query escalated to media desk. | 2019-11-29 12:46:10 | [@bongadlulane, query, escalated, media, desk.]|


## Singularity Group 10 Members - Contributing Authors
Author='Mangaliso Makhoba, Zanele Gwamanda, Nkululeko Mthembu, Letlhogile Mothoagae, Bryan Green',
Author_email='makhoba808@gmail.com, zanelegwamanda99@gmail.com, nsm.branding@gmail.com, lot.mothoagae@gmail.com, bryangreen290@gmail.com'

## Project Continuity
This is an ongoing, live project and data may be updated from time to time.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

