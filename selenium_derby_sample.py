import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# race table
race_table = pd.read_html(
    "http://race.netkeiba.com/?pid=race_old&id=c201805021210",
    header=0,
)
race_table = race_table[0]
race_table = race_table.drop(0, axis=0)
race_table = race_table.drop(1, axis=0)
print(race_table)

horse_names = []
for i, horse_name in enumerate(race_table['馬名']):
    print(i, horse_name)
    horse_names.append(horse_name)

# horses data
driver = webdriver.Firefox()
elem_0 = driver.get("http://race.netkeiba.com/?pid=race_old&id=c201805021210")

for horse_name in horse_names:
    print("****************" + str(horse_name) + "****************")
    time.sleep(2)
    elem_1_link = driver.find_element_by_link_text(horse_name)
    elem_1_url = elem_1_link.get_attribute("href")

    time.sleep(2)

    elem_2 = driver.get(elem_1_url)
    elem_2_link = driver.find_element_by_link_text('戦績')
    elem_2_url = elem_2_link.get_attribute("href")

    elem_3 = driver.get(elem_2_url)

    current_url = driver.current_url
    horse_detail = pd.read_html(current_url, header=0)
    horse_detail = horse_detail[0]
    print(horse_detail)
        
    time.sleep(2)
    
    driver.get("http://race.netkeiba.com/?pid=race_old&id=c201805021210")

driver.close()
