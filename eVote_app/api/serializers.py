#rest-django imports
from rest_framework import serializers
from django.db.models import Count
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
#in-app imports
from eVote_app.models import (PoliticalElection, PoliticalParty,
                              Citizen, Vote)



class PoliticalPartySerializer(serializers.ModelSerializer):

    class Meta:
        model = PoliticalParty
        exclude = ['politicanelections']
    
class PoliticalElectionSerializer(serializers.ModelSerializer):

    choices = PoliticalPartySerializer(many=True)

    class Meta:
        model = PoliticalElection
        fields = "__all__" 

class UserSerializer(serializers.ModelSerializer): #this is for registration...
    name = serializers.CharField(source="first_name")
    uniquenumber = serializers.CharField(max_length=200,write_only=True)
    class Meta:

        model = User
        fields = ["username","password","uniquenumber","name"]
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def save(self):
        if Citizen.objects.filter(uniquenumber=self.validated_data["uniquenumber"]).exists():
            raise serializers.ValidationError({"error":"uniquenumber is used"})
        if Citizen.objects.filter(username=self.validated_data["username"]).exists():
            raise serializers.ValidationError({"error":"username is used"})
        user = User.objects.create(username = self.validated_data["username"])
        user.set_password(self.validated_data["password"])
        user.save()
        token = Token.objects.create(
            user = user
        )

        citizen = Citizen.objects.create(
            user = user,
            name = self.validated_data["first_name"],
            username = self.validated_data["username"],
            uniquenumber = self.validated_data["uniquenumber"]
        )
    
    

class CitizenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Citizen
        fields = ["id","name","username","user"]




    
    


    

    