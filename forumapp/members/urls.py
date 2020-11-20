from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    #url for registration page
    path('register/', UserRegisterView.as_view(), name='register'),
]
