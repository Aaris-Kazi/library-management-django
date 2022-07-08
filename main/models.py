from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=50)    
    status = models.CharField(max_length=50,default='Available')   
    def __str__(self):
        return self.book_name+""+str(self.status)