from django.urls import path;
from . import views;

urlpatterns=[
    # path('',view=views.file_upload,name='file_upload'),
    # path('<int:file_id>',view=views.delete_file,name='delete_file'),
    path('',views.file_list,name='file_list'),
    path('create/',views.file_create,name='file_create'),
    path('<int:file_id>/',views.file_detail,name='file_detail'),
    path('<int:file_id>/download/',views.file_download,name='file_download'),
    path('<int:file_id>/edit/',views.file_update,name='file_update'),
    path('<int:file_id>/delete/',views.file_delete,name='file_delete'),
    ]

