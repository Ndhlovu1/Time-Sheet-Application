"""CapricornProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TimeSheetsApp.urls')),
    path('api/manager/', include('ManagerApp.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
    
]

"""
Successfully Allows User Self Registration
http://localhost:8000/auth/users/ works successfully

Allows users to be added to a group(Managers)
http://localhost:8000/api/groups/manager/users

"""



#Djoser Handy endpoints
"""

/users/
/users/me/
/users/confirm/
/users/resend_activation/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username/confirm/
/token/login/
/token/logout/

to access them -> localhost:8000/auth infront of this url



"""
