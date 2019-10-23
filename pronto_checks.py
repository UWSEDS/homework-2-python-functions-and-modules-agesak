import pandas as pd


def read_in_data(url):
    df = pd.read_csv(url)
    return df


def test_create_dataframe(df, cols):

    conditions = []

    # Does the dataframe contain only cols?
    conditions.append(list(df) == cols)

    # Do the values in each column have the same python type?
    col_types = []
    for col in list(df):
        types = []
        for index, row in df[col].iteritems():
            types.append(type(row))
        types = set(types)    
        col_types.append(len(types)==1)
    conditions.append(col_types)

    # Are there at least 10 rows in the dataframe?
    conditions.append(len(df) >= 10)

    return all(conditions) == True
