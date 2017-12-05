#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import pandas as pd


def generate_racetable(url, csvfile):
# @test racename is jc
    race_html = pd.read_html(url)
    race_table = race_html[0]
    # @test race_table is None
    print(race_table)

    return race_table.to_csv(csvfile, index=None)


if __name__ == '__main__':
    _URL = "http://race.netkeiba.com/?pid=race&id=p201705050811&mode=top"
    _CSV_FILE = '2017_jc_race_table.csv'
    execute = generate_racetable(_URL, _CSV_FILE)
