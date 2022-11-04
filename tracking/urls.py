from django.urls import path
from . import views


app_name = 'tracking'
urlpatterns = [
	path('', views.Home.as_view()),
]