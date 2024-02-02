from django.urls import path, include
from .views import authView, home, myLogOut, shopping

urlpatterns = [
 path("", home, name="home"),
 path("home/", home, name="home"),
 path("logout/", myLogOut, name="mylogOut"),
 path("signup/", authView, name="authView"),
 path("shopping/",shopping, name="shopping"),
 path("accounts/", include("django.contrib.auth.urls")),
]
