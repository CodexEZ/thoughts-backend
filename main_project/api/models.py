from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True,null=False)
    email = models.CharField(max_length=100,null = False)
    password = models.CharField(max_length=100,null=False)
class Posts(models.Model):
    user = models.ForeignKey(Users, on_delete= models.CASCADE)
    title = models.TextField(null=False)
    desc = models.TextField(null=False)
    pub_date = models.DateTimeField(auto_now_add=True)

