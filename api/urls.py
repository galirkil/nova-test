from django.urls import path
from api.views import create_gdrive_file

app_name = 'api'

urlpatterns = [
    path('create-gdrive-file/', create_gdrive_file)
]
