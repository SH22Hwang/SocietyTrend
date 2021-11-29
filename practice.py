import requests
from bs4 import BeautifulSoup

url = 'http://scholar.dkyobobook.co.kr/searchExtAcademy.laf?vendorGb=05&academyCd=20580'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select_one('div.searchExtAcademy')
    titles = div.select('div.paper_info > div.paper_box > dl > dt > a')

    for title in titles:
        print(title.get_text())

else :
    print(response.status_code)