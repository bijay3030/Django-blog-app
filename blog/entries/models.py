from django.db import models

#The most direct way to create users is to use the included create_user() helper function:
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User,on_delete=models.CASCADE)

    
    
       
    