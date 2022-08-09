from django.db import models

# Create your models here.
class detail(models.Model):
    Name = models.CharField(max_length=50)
    Date = models.DateField()
    Message = models.CharField(max_length=1000)
    Email = models.EmailField(max_length=60)


    def __str__(self):
        return self.Name
        
