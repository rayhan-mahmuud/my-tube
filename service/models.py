from django.db import models
from embed_video.fields import EmbedVideoField


class Folder(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subfolders', null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Video(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255, null=True)
    url = EmbedVideoField()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='videos')
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.folder.name}/{self.name}"
    
    
    

    
    

