from django.urls import path
from .views import HomeView, PostDetailView, AddPostView

urlpatterns = [
    #url for home page
    path('', HomeView.as_view(), name="home"),
    #url for postDetails page
    path('post/<int:pk>', PostDetailView.as_view(), name="postDetail"),
    #url for addPost page
    path('addPost/', AddPostView.as_view(), name='addPost')
]
