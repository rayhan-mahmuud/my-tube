from django.urls import path
from service.views import IndexView, FolderDetailView, SubfolderCreateView


app_name = 'service'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("folder/<int:folder_id>/", FolderDetailView.as_view(), name='folder_view'),
    path("folder/<int:folder_id>/create-subfolder/", SubfolderCreateView.as_view(), name='subfolder_create'),
]
