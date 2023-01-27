from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('eVote_app.api.urls')),
    path('users/',include('usershandler_app.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
