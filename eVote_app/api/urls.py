#rest-django imports
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
#in-app imports 
from eVote_app.api.views import (CitizenList, PoliticalElectionVote)


router = DefaultRouter()
router.register("elections",PoliticalElectionVote,basename="elections")
urlpatterns = [
    path("",include(router.urls)),
    #path("",PoliticalElectionList.as_view(),name="list"),
    #path("election/<int:pk>/",PoliticalElectionVote.as_view({"get":"retrieve"}),name="election-detail"),
    path("citizenlist/",CitizenList.as_view(),name="list"),  

]
