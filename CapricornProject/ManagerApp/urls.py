from django.urls import path
from . import views

urlpatterns = [    
    path('', views.ViewTimeSheets.as_view()),
    path('edit-time-sheet/<int:pk>', views.SingleTimeSheet.as_view()),
    path('admin-edit/', views.AdminEditView.as_view()),
]




