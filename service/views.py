from django.shortcuts import render, redirect
from django import views

from service.models import Folder, Video
from service.forms import FolderForm, VideoForm

class IndexView(views.View):
    form_class = FolderForm
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        folders = Folder.objects.filter(parent=None)
        context = {
            "folders": folders,
            "form": form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('service:index')
        
        folders = Folder.objects.filter(parent=None)
        context = {
            "folders": folders,
            "form": form,
            "errors": form.errors,
        }
        return render(request, self.template_name, context)
        

# class FolderCreateView(views.View):
#     form_class = FolderForm
#     template_name = "newfolder.html"
    
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         folders = Folder.objects.filter(parent=None)
#         return render(request, self.template_name, context={'form':form, 'folders':folders})
    
class FolderDetailView(views.View):
    
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
    
    
# Todo: Add and remove folder functionality
