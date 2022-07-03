from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    discriptions = models.TextField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.discriptions
