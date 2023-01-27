#rest-django imports
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
#in-app imports
from eVote_app.api.serializers import (PoliticalElectionSerializer, UserSerializer,
                                       CitizenSerializer,PoliticalPartySerializer)
from eVote_app.models import (PoliticalElection, Citizen,
                              Vote, PoliticalParty)
from eVote_app.api.permissions import (IsUserOrReadOnly, IsAdminOrReadOnly)




class CitizenList(generics.ListAPIView):

    queryset = Citizen.objects.all().select_related("user")
    serializer_class = CitizenSerializer

    #when i set queryset like this,
    #in one query he get and Citizen and User,
    #i cannot get response without select_related,
    #and getting response is optimized... 


'''
class PoliticalElectionList(generics.ListAPIView):

    queryset = PoliticalElection.objects.filter(
        Q(end__gte=timezone.now())   & 
        Q(start__lte=timezone.now())).prefetch_related("choices")
    serializer_class = PoliticalElectionSerializer
'''

class PoliticalElectionVote(viewsets.ModelViewSet):

    queryset = PoliticalElection.objects.filter(
        Q(end__gte=timezone.now())   & 
        Q(start__lte=timezone.now())).prefetch_related("choices","voteelection")
    serializer_class = PoliticalElectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    
    @action(
        detail=True,
        methods=["POST"],
        permission_classes = [IsAuthenticated]
    )
    def vote(self,request,pk=None):
        election = get_object_or_404(PoliticalElection,pk=pk)
        if election.start>timezone.now():
            return Response({"time":f"elections starts in {election.start}"},
                            status = status.HTTP_403_FORBIDDEN)
        if election.end<timezone.now():
            return Response({"time":f"elections ended in {election.end}"},
                            status = status.HTTP_403_FORBIDDEN)    
        user = request.user
        party = get_object_or_404(PoliticalParty,pk=request.data["partyid"])
        if Vote.objects.select_related("election","user").filter(election=election,user=user).exists():
            return Response({"forbbiden":"already voted"},status=status.HTTP_403_FORBIDDEN)
        vote = Vote.objects.create(
            user=user,
            election = election,
            politicalparty=party    
        )
        vote.save()
        
        return Response({"msg":"successfully voted"},status=status.HTTP_201_CREATED)
        #creating vote object with all requirments

    @action(
        detail=True,
        methods=["get"],
        permission_classes = [IsAdminUser],
    )
    def get_votes(self,request,pk=None):
        election = get_object_or_404(PoliticalElection,pk=pk)
        data = {}
        votes = Vote.objects.filter(election=election).select_related("politicalparty","election","user")
        for party in election.choices.all():
            data[party.name]=0
        for vote in votes:
            if vote.politicalparty.name in data:
                data[vote.politicalparty.name]+=1
                continue

            
        return Response(data)










        


        

        
        