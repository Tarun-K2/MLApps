def clean_data(df):
    df = df.na.drop(how='any')
    df = df.filter(df['amount'].isNotNull())
    return df


