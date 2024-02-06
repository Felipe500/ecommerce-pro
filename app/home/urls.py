from django.urls import path
from .views import WebsiteView, home


urlpatterns = [
    path("home", WebsiteView.as_view(), name="index"),
    path("", home, name="home"),
]
