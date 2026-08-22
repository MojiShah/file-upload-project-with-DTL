from django.urls import path;
from . import views;

urlpatterns=[
    path('',view=views.file_upload,name='file_upload'),
    path('<int:file_id>',view=views.delete_file,name='delete_file'),
    ];

