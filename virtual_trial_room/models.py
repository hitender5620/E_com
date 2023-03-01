from django.db import models
from django.db.models.fields.files import Imagefield

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image=models.ImageField( upload_to="images")
    content=models.TextField()
    
    def__str_(self):
    return self.title

    def_cam(self):
    return self.title    
        
    