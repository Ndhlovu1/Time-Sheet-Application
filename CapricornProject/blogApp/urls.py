from django.urls import path
from . import views

#Application namespace
app_name = 'blogApp'

urlpatterns = [    
    #path('', views.list_posts, name='list_posts'),
    path('',views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.single_post, name='single_post'),
    path('<int:post_id>/share/',views.share_post, name="share_post"),
]



