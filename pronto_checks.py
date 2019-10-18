from urllib.request import urlopen
from io import StringIO
import pandas as pd


def read_in_data():

    # read in pronto data
    link = "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
    f = urlopen(link)
    df = f.read()

    # convert to dataframe
    s = str(df, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)

    return df


def test_create_dataframe(df, cols):

    conditions = []

    # Does the dataframe contain only cols?
    conditions.append(list(df) == cols)

    # Do the values in each column have the same python type
    # conditions.append(len(df.dtypes.unique()) == 1)

    # or?
    same_type = True
    for col in list(df):
        if len(df[col].dtype) != 0:
            same_type = False
    conditions.append(same_type)

    # Are there at least 10 rows in the dataframe?
    conditions.append(len(df) >= 10)

    return all(conditions) == True
