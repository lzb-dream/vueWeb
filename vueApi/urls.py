from django.urls import path,include
from .views import wySwiper,FountMusic,SongsIntroduceData,SongsListData
urlpatterns = [
    path('swiper',wySwiper.as_view()),
    path('fountMusic',FountMusic.as_view()),
    path('songsIntroduceData/<str:id>',SongsIntroduceData.as_view()),
    path('songsListData/<str:id>', SongsListData.as_view())
]