from django.urls import path
from . import views
import django.contrib.auth.urls

urlpatterns = [
#    path('', views.index, name='index'),
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
