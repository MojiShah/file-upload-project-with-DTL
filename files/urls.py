from django.urls import path;
from . import views;

urlpatterns=[
    # path('',view=views.file_upload,name='file_upload'),
    # path('<int:file_id>',view=views.delete_file,name='delete_file'),
    path('',views.file_list,name='file_list'),
    path('create/',views.file_create,name='file_create'),
    path('<int:file_id>/',views.file_detail,name='file_detail')
    ];

