import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

wd=webdriver.Chrome('C:/Users/장경빈/PycharmProjects/crawling/WebDriver/chromedriver.exe')
wd.get("https://www.kyochon.com/shop/domestic.asp")
select=Select(wd.find_element(By.ID,'sido1'))
result=list()
for x in range(1,len(select.options)):
    select = Select(wd.find_element(By.ID, 'sido1'))
    sido=select.options[x].text
    select.select_by_index(x)
    select2=Select(wd.find_element(By.ID,'sido2'))
    for y in range(len(select2.options)):
        select2 = Select(wd.find_element(By.ID, 'sido2'))
        gungu=select2.options[y].text
        select2.select_by_index(y)
        wd.execute_script("search()")
        try:
            store_list=wd.find_elements(By.CLASS_NAME, 'store_item')
        except:
            continue
        store_info=list()
        for info in store_list:
            store_info.append(info.text.split("\n"))
        #print(store_info)
        for z in range(0,len(store_info)):
            result.append((store_info[z][0],sido, gungu,store_info[z][1]))
        #print(len(store_info))
        time.sleep(0.5)

    #print(result)
CB_tbl = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'address'))
CB_tbl.to_csv('./kyochon.csv', encoding='cp949', mode='w', index = True)

