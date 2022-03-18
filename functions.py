def filter_df_dates (df, start_date, end_date):
    start_date = start_date
    end_date = end_date
    new_df = df[(df['date'] > start_date) & (df['date'] <= end_date)]
    return new_df
def ready_to_plot (df, col1, col2):
    grouped_df = df.groupby(col1)
    df = grouped_df.sum()
    df = df.reset_index()
    df = df.sort_values(col2, ascending=False)
    return df
