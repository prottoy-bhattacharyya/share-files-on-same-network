from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("download/<str:file_name>", views.download, name="download")
]
