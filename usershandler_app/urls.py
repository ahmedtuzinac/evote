#django-rest imports
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
#in-app imports
from usershandler_app.views import (logoutuser, UserRegistration)

urlpatterns = [
    path("register/", UserRegistration.as_view(),name="register"),
    path("login/", obtain_auth_token,name="login"),
    path("logout/",logoutuser,name="logout")
]
