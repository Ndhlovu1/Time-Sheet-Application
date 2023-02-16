from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeSheetView, name="TimeSheet"),
]



