#django-rest imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#in-app imports





class PoliticalElection(models.Model):

    name = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField() 

    def __str__(self):
        return self.name

class PoliticalParty(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    politicanelections = models.ManyToManyField(PoliticalElection,
                                                related_name="choices")

    def __str__(self):
        return self.name

class Citizen(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=50)
    uniquenumber = models.CharField(max_length=100,blank=True,null=True)
    
class Vote(models.Model):

    election = models.ForeignKey(PoliticalElection,
                                 on_delete=models.CASCADE,
                                 related_name="voteelection")

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="voteuser")
    
    politicalparty = models.ForeignKey(PoliticalParty,
                                       on_delete=models.CASCADE,
                                       related_name="partyvotes")

    def __str__(self):
        return self.user.username + " " + self.election.name

    




