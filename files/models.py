from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='uploads/');
    uploaded_at = models.DateTimeField(auto_now_add=True);
    
    @property
    def is_image(self):
        return self.file.name.lower().endswith(
            (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg")
        )
    
    def __str__(self):
        return self.file.name