from django.urls import path
from . import views
y
urlpatterns = [path('', views.homePageView, name='home'),]
