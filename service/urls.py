from django.urls import path
from service.views import IndexView, FolderView


app_name = 'service'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("folder/<int:folder_id>/", FolderView.as_view(), name='folder_view'),
]
