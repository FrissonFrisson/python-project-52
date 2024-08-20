from django.db import models
from django.contrib.auth.models import User



class Task_status(models.Model):
    name = models.CharField(max_length=200, unique=True) # название статьи
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Label(models.Model):
    name = models.CharField(max_length=200, unique=True) # название статьи
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class LabelInfo(models.Model):
    task = models.ForeignKey('Task', on_delete=models.PROTECT)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    date_joined = models.DateTimeField(auto_now_add=True)
    

class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    descriptions = models.TextField()
    status = models.ForeignKey(Task_status, on_delete = models.PROTECT)
    label = models.ManyToManyField(Label, through="LabelInfo")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    performer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_performed')

    
    def __str__(self):
        return self.name