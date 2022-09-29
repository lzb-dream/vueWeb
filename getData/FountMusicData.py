from bs4 import BeautifulSoup
import requests
import re
# 图片，播放量，标题
# 爬虫一定要去掉井号
url = 'https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
result = requests.get(url).text
beau = BeautifulSoup(result,"html.parser")
FountMusicData = []
htmlData = beau.select('ul[class="m-cvrlst f-cb"]>li')
for i in htmlData:
    item = {}
    photo = i.select('img[class="j-flag"]')[0]['src']
    amountOfPlay = str(i.select('span[class="nb"]')[0].string)
    title = str(i.select('a[class="tit f-thide s-fc0"]')[0].string)
    id = i.select('a[class="icon-play f-fr"]')[0]['data-res-id']
    item['photo'] = photo
    item['amountOfPlay'] = amountOfPlay
    item['title'] = title
    item['id'] = id
    FountMusicData.append(item)
