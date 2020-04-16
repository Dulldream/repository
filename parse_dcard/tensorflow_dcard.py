from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(path)
url = "https://www.dcard.tw/f"
driver.get(url)

#在搜尋的輸入框內輸入文字
inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('tensorflow')

#點擊搜尋按鈕
driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)

#擷取內容，並解析成html結構樹
html = driver.page_source
soup = bs(html, 'html.parser')

#獲得文章的看板、作者、時間
data = soup.find_all('span', {'class':'sc-6oxm01-2 hiTIMq'})
meta_datas = []
for x in data :
    meta_datas.append(x.text)
print(meta_datas)

#從meta_datas裡面挑出看板
forums = []
author = []
times = []
for i in range(len(meta_datas)):
    if i % 3 == 0 :
        if meta_datas[i] == '軟體工程師' :
            forums.append(meta_datas[i])
        # forums.append(meta_datas[i])
    if i % 3 == 1 :
        author.append(meta_datas[i])
    if i % 3 == 2 :
        times.append(meta_datas[i])

titles = []
data = soup.find_all('h2', {'class':'sc-1v1d5rx-3 eihOFJ'})
for x in data :
    titles.append(x.text)
print(titles)

#獲得文章相對連結
data = soup.find_all('a', {'class':'sc-1v1d5rx-4 gCVegi'})
hrefs = []
for x in data:
    hrefs.append(x['href'])

# 從相對連結及url組成相對連結
links = []
for href in hrefs :
    links.append(urljoin(url, href))
print(links)

#印出結果
for i in range(len(forums)):
    print(forums[i], titles[i], links[i])
