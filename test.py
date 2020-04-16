
import requests
from data import Location
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)  #向html提出get要求

josn_content = html_content.json() #轉成json

# print(html_content.text)

records = josn_content.get("records")
location = records.get('location')
# print(location)
allLocations = []
for item in location:
    l = Location()
    l.from_json(item)
    allLocations.append(l)
    print(l.__dict__)
print(allLocations)

    #取得觀測資料
    # weatherElement = item.get('weatherElement')
    # for element in weatherElement:
    #     elementName = element.get('elementName')
    #     elementValue = element.get('elementValue')
    #     print(elementName,elementValue)