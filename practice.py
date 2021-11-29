import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'http://scholar.dkyobobook.co.kr/searchExtAcademy.laf?vendorGb=05&academyCd=20580'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

select = Select(driver.find_element_by_name('volSel'))

trendList = []

response = select.select_by_value('144521')
# response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
div = soup.select_one('div.searchExtAcademy')
titles = div.select('div.paper_info > div.paper_box > dl > dt > a')

for title in titles:
    trendList.append(title.get_text())
print(trendList)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     div = soup.select_one('div.searchExtAcademy')
#     titles = div.select('div.paper_info > div.paper_box > dl > dt > a')
#
#     for title in titles:
#         trendList.append(title.get_text())
#
#     print(trendList)
# else:
#     print(response.status_code)
