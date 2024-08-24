from django.urls import path
from service.views import IndexView, FolderDetailView


app_name = 'service'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("folder/<int:folder_id>/", FolderDetailView.as_view(), name='folder_view'),
]
