from django import forms

from service.models import Folder, Video


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent', 'is_public']
        

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ['added_at', 'modified_at']