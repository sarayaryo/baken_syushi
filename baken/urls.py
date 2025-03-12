from django.urls import path
from . import views

app_name = 'baken'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
]