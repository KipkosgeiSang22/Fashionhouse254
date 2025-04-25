from django.urls import path
from .import views

app_name= 'more_details'
urlpatterns = [
path("<int:pk>", views.detail, name="detail"),
]