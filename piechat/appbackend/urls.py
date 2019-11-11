from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name="api-token-auth"),
    path('signup/', views.CreateUserView.as_view(), name="sign up user"),
    path('chats/', views.ChatsView.as_view(), name="user chats"),
    path('hello/', views.HelloView.as_view(), name="hello")
]