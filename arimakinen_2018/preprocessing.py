import gc


def strings_to_sec(time_strings):
    convert_strings = time_strings.split(':')
    convert_strings = int(convert_strings[0]) * 60 + float(convert_strings[1])

    return convert_strings


def separate_ranking(ranking_strings, index):
    convert_strings = ranking_strings.split('-')[index]

    return convert_strings


def separate_diff(weight_strings):
    print(weight_strings)
    convert_strings = weight_strings.split('(')
    print('convert_strings')
    print(convert_strings)
    weight = convert_strings[0]
    print('weight')
    print(weight)
    if convert_strings[1].find('+') >= 0:
        print('+ exists')
        diff = convert_strings[1].replace('+', '')
        diff = diff.split(')')[0]
        print('diff')
        print(diff)
    else:
        print('not +')
        diff = convert_strings[1].split(')')[0]
        print('diff')
        print(diff)

    return diff


def separate_weight(weight_strings):
    convert_strings = weight_strings.split('(')
    weight = convert_strings[0]

    return weight


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
