from django.urls import path
from facerecognition import views

urlpatterns = [
    path("", views.index, name="facerecognition")
]


