from rest_framework import routers
from questions.views import QuestionViewSet, QuestionRewardListApi,QuestionRewardCreateApi,UserRewardGetApi
from django.urls import path

router = routers.SimpleRouter()
router.register(r'list', QuestionViewSet)

urlpatterns = router.urls

urlpatterns+=[
    path('getreward/', QuestionRewardListApi.as_view()),
    path('createreward/', QuestionRewardCreateApi.as_view()),
    path('getuserreward/', UserRewardGetApi.as_view()),
]