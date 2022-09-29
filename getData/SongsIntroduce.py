from bs4 import BeautifulSoup
import requests
import re


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
# if __name__ == '__main__':
#     id = '391125700'
#     getSongList(id)