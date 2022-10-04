from rest_framework.views import Response,APIView
from getData.CrawlData import getSongsIntroduce,getSongList,fountMusicData,getLyrics
class wySwiper(APIView):
    def get(self,request,*args,**kwargs):
        data = ['https://img.51miz.com/Element/00/96/40/24/52d04760_E964024_f92f3a97.jpg',
                'https://img.zcool.cn/community/01ca1357eb1791a84a0e282bee6d49.jpg@1280w_1l_2o_100sh.jpg',
                'https://img.zcool.cn/community/011e3458df705ca801219c77279b96.jpg@1280w_1l_2o_100sh.jpg',
                'https://img.zcool.cn/community/013add5779dc220000012e7e96dc60.jpg@1280w_1l_2o_100sh.jpg']
        return Response({'data':data})

class FountMusic(APIView):
    def get(self,request,*args,**kwargs):
        FountMusicData = fountMusicData()
        return Response({'FountMusicData': FountMusicData})

class SongsIntroduceData(APIView):
    def get(self,request,id):
        songsIntroduce = getSongsIntroduce(id)
        return Response({'songsIntroduce': songsIntroduce})

class SongsListData(APIView):
    def get(self,request,id):
        songsListData = getSongList(id)
        return Response({'songsListData': songsListData})

class GetLyrics(APIView):
    def get(self, request, id):
        getLyricsData = getLyrics(id)
        return Response({'getLyricsData': getLyricsData})