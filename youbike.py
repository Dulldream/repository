import requests
url = "http://opendata.hccg.gov.tw/dataset/1f334249-9b55-4c42-aec1-5a8a8b5e07ca/resource/3f2d8472-7bae-48d0-909f-546591a34d34/download/20191231090605186.json"
html_content = requests.get(url)
print(html_content.status_code)
josn_content = html_content.json()

allSites = []
for josn_data in josn_content :
    site = Site()
    site.from_josn(josn_data)
    allSites.append(site)










