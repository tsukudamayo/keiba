import gc

import pandas as pd

from preprocessing import (separate_diff, separate_ranking, separate_weight,
                           strings_to_sec)


def load_data(csv_file):
    df = pd.read_csv(
        csv_file,
        encoding='shift-jis',
        dtype='object',
    )

    return df


def main():

    df = load_data('past_race_data.csv')

    # null check
    print(df.isnull().sum())

    # drop null value columns
    drop_idx = ['着差', 'ﾀｲﾑ指数', '調教ﾀｲﾑ', '厩舎ｺﾒﾝﾄ', '備考', '賞金(万円)']
    df = df.drop(drop_idx, axis=1)

    # drop null rows
    df = df.dropna()
    print(df.isnull().sum())

    # convert rank
    for i in range(4):
        columns_string = 'rank_' + str(i)
        df[columns_string] = df['通過'].apply(lambda x: separate_ranking(x, i))
    del df['通過']

    # convert time to second
    df['second'] = df['タイム'].apply(lambda x: strings_to_sec(x))
    del df['タイム']

    # calculation "first_harf" seconds
    df['上り'] = df['上り'].astype(float)
    df['first_half'] = df['second'] - df['上り']

    # separate weight and diff
    df['weight'] = df['馬体重'].apply(lambda x: separate_weight(x))
    df['diff'] = df['馬体重'].apply(lambda x: separate_diff(x))

    gc.collect()

    print(df.isnull().sum())
    print(df.head())

    df.to_csv('preprocessed_race_data.csv')


if __name__ == '__main__':
    main()
