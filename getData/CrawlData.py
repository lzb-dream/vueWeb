import json
from bs4 import BeautifulSoup
import requests
import re
# 图片，播放量，标题
# 爬虫一定要去掉井号
def fountMusicData():
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
    return FountMusicData

# 作者昵称
# 作者头像
# 介绍
# 评论数量
# 分享数量
def getSongsIntroduce(id):
    data = {}
    url = f'https://music.163.com/playlist?id={id}'
    result = requests.get(url).text
    beau = BeautifulSoup(result, "html.parser")
    nickname = str(beau.select('a[class="s-fc7"]')[0].string)
    headPortrait = str(beau.select('a[class="face"]>img')[0]['src'])
    introduce = beau.select('p[id="album-desc-more"]')[0].get_text()
    commentsNumber = str(beau.select('span[id="cnt_comment_count"]')[0].string)
    shareNumber = str(beau.select('a[class="u-btni u-btni-share"]>i')[0].string)
    shareNumber = re.findall('\d+', shareNumber)[0]
    collectionNumber = beau.select('a[class="u-btni u-btni-fav"]')[0]['data-count']
    data['nickname'] = nickname
    data['headPortrait'] = headPortrait
    data['introduce'] = introduce
    data['commentsNumber'] = commentsNumber
    data['shareNumber'] = shareNumber
    data['collectionNumber'] = collectionNumber
    return data


# 歌名
# 歌手
# 时长
# 收藏数
def getSongList(id):
    url = f'https://music.163.com/playlist?id={id}'
    response = requests.get(url).text
    beau = BeautifulSoup(response,"html.parser")
    sonNameList = beau.select('ul[class="f-hide"]>li>a')
    data = []
    for i in sonNameList:
        songName = i.string
        songId = i['href']
        response = requests.get(f'https://music.163.com{songId}').text
        makeName = re.findall(r'<p class="des s-fc4">歌手：<span title="(.*)"><a class="s-fc7"',response)[0]
        songImg = BeautifulSoup(response,"html.parser").select('div[class="u-cover u-cover-6 f-fl"]>img')[0]['src']
        a = {'songName':songName, 'makeName':makeName, 'songId':songId.split('=')[1],'songImg':songImg}
        data.append(a)
    return data

# 获取歌词
def getLyrics(id):
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Requested-With': "XMLHttpRequest"
    }
    data = {
        'input': id,
        'filter': 'id',
        'type': 'netease',
        'page': '1'
    }
    url = "https://music.liuzhijin.cn/"
    rep = requests.post(url,headers=headers,data=data).json()
    return rep['data'][0]['lrc']