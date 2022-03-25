from django.db import models
from django.contrib.auth.models import User
from datetime import datetime #models.DateTimeField yerine bunu da kullanabiliriz.
### whenever you make changes in models.py dont forget to make migrations


class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']