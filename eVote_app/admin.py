from django.contrib import admin

#in-app imports
from eVote_app.models import (PoliticalElection, PoliticalParty,
                              Citizen, Vote)

admin.site.register(PoliticalElection)
admin.site.register(PoliticalParty)
@admin.register(Citizen)

class CitizenAdmin(admin.ModelAdmin):

    list_display = ("name","uniquenumber",)
    search_fields = ("uniquenumber","name",)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):

    list_display = ("user","election")
    search_fields = ("user",)
    

