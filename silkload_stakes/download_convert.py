# _*_ codings: utf-8 _*_
import pandas as pd


def download_race_table():
    """ read race table """
    race_table = pd.io.html.read_html(
        'https://race.netkeiba.com/?pid=race_old&id=c201908020211', header=0)
    race_table = race_table[0]
    print('race_table', race_table)
    race_table.to_csv('race_table.csv', encoding='SHIFT-JIS')
    return race_table


def merge_past_race_data(start_offset, end_offset):
    """ https://db.netkeiba.com/race/199708030211/ """
    race_ids = range(start_offset, end_offset + 1)
    print(race_ids)

    past_race_data = pd.DataFrame({})
    for race_id in race_ids:
        if race_id == 1996:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '08030411/',
                header=0)
        elif 1997 <= race_id <= 1999:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '08030211/',
                header=0)
        elif 2011 <= race_id <= 2012:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '08020111/',
                header=0)
        elif 2013 <= race_id:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '08020211/',
                header=0)
        else:
            race_data = pd.io.html.read_html(
                'https://db.netkeiba.com/race/' + str(race_id) + '08020411/',
                header=0)
        print('race_data')
        print(race_data)
        race_data = race_data[0]
        print('race_data', race_data.head())
        print('race_data_length', len(race_data))
        concat_data = pd.concat([past_race_data, race_data], axis=0)
        past_race_data = concat_data
    print('past_race_data_length', len(past_race_data))
    past_race_data.to_csv('past_race_data.csv', encoding='SHIFT-JIS')

    return past_race_data


def main():
    race_table = download_race_table()
    past_race_data = merge_past_race_data(1996, 2018)


if __name__ == '__main__':
    main()
