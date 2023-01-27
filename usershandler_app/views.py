#django-rest imports
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
#in-app imports 
from eVote_app.api.serializers import UserSerializer


class UserRegistration(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logoutuser(request):    
    try:
        token = Token.objects.get(user=request.user)
        token.delete()

    except Token.DoesNotExist:
        return Response({"msg":"invalid user"})
        
    return Response({"msg":"user successfully logged out"})



