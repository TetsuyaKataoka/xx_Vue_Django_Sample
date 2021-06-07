from django.urls import include, path
from .views import *

app_name = 'api'

urlpatterns = [
    path('get/', GetTestAPI.as_view()),
    path('listMembers/', ListMembers.as_view()),
    path('createMember/', CreateMember.as_view()),
    path('listPositions/', ListPositions.as_view()),
    path('createPosition/', CreatePosition.as_view()),
    path('listMemberPositions/', ListMemberPositions.as_view()),
    path('createMemberPosition/', CreateMemberPosition.as_view()),
]