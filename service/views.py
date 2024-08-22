from django.shortcuts import render
from django import views

from service.models import Folder, Video

class IndexView(views.View):
    
    def get(self, request, *args, **kwargs):
        
        folders = Folder.objects.filter(parent=None)
        context = {
            "folders": folders,
        }
        return render(request, template_name='index.html', context=context)
    
class FolderView(views.View):
    
    def get(self, request, folder_id, *args, **kwargs):
        folder = Folder.objects.get(pk=folder_id)
        videos = folder.videos.all()
        subfolders = folder.subfolders.all()
        context = {
            "folder": folder,
            "subfolders": subfolders,
            "videos": videos,
        }
        return render(request, template_name='folder_view.html', context=context)