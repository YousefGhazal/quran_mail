from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) :
        return self.email

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]
        
    def __str__(self) :
        return self.email
