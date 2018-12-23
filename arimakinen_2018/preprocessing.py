import gc


def strings_to_sec(time_strings):
    convert_strings = time_strings.split(':')
    convert_strings = int(convert_strings[0]) * 60 + float(convert_strings[1])

    return convert_strings


def separate_ranking(ranking_strings, index):
    convert_strings = ranking_strings.split('-')[index]

    return convert_strings


def null_check(df):
    print(df.isnull().sum())


def drop_columns(df, columns):
    drop_df = df.drop(columns, axis=1)

    return drop_df


def drop_null_value(df):
    drop_null_value = df.dropna()

    return drop_null_value


def exec_gc():
    gc.collect()

    return
