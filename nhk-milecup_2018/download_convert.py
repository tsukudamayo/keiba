# _*_ codings: utf-8 _*_
import pandas as pd


def download_race_table():
    """ read race table """
    race_table = pd.read_html(
        'http://race.netkeiba.com/?pid=race_old&id=c201805020611&mode=top',
        header=0,
    )
    race_table = race_table[0]
    print('race_table', race_table)
    race_table.to_csv('race_table.csv',
                      encoding='SHIFT-JIS')

    return race_table


def merge_past_race_data(start_offset, end_offset):
    """ http://db.netkeiba.com/race/201705020611/ """
    race_ids = range(start_offset, end_offset+1)
    print(race_ids)

    past_race_data = pd.DataFrame({})
    for race_id in race_ids:
        print('year:', race_id)
        if 1997 <= race_id <= 1999:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '05020811/',
                header=0
            )
        elif race_id == 2002:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '05030611/',
                header=0
            )
        elif race_id == 2003:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '05010611/',
                header=0
            )
        else:
            race_data = pd.io.html.read_html(
                'http://db.netkeiba.com/race/' + str(race_id) + '05020611/',
                header=0
            )
        race_data = race_data[0]
        print('race_data', race_data.head())
        print('race_data_length', len(race_data))
        concat_data = pd.concat(
            [past_race_data, race_data],
            axis=0
        )
        past_race_data = concat_data
    print('past_race_data_length', len(past_race_data))
    past_race_data.to_csv('past_race_data.csv',
                           encoding='SHIFT-JIS')

    return past_race_data


def main():
    race_table = download_race_table()
    past_race_data = merge_past_race_data(1997, 2017)


if __name__ == '__main__':
    main()
