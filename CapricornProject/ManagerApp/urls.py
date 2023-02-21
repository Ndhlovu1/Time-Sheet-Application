from django.urls import path
from . import views

urlpatterns = [    
    path('admin-edit/', views.ViewTimeSheets.as_view()),
    path('admin-edit/<int:pk>', views.SingleTimeSheet.as_view()),
    path('', views.AdminEditView.as_view()),
]




