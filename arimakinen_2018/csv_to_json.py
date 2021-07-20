import os
import codecs
import json
import pandas as pd
from analyze_past_data import load_data

def csv_to_json(filepath: str):
    filename, ext = os.path.splitext(filepath)
    data = json.loads(load_data(filepath).to_json())
    with codecs.open(filename + ".json", "w", "utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=False)

    return 

def main():
    sample_race_data = "./past_race_data.csv"
    sample_race_table = "./race_table.csv"
    csv_to_json(sample_race_data)
    csv_to_json(sample_race_table)
          

if __name__ == "__main__":
    main()
