from django.urls import path
from service.views import IndexView, FolderDetailView


app_name = 'service'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    # path("new-folder/", FolderCreateView.as_view(), name='newfolder'),
    path("folder/<int:folder_id>/", FolderDetailView.as_view(), name='folder_view'),
]
