from django.db import models
import datetime
from tinymce.models import HTMLField

class category(models.Model):
    newscategory=models.CharField(null=False,max_length=50)

    def __str__(self) -> str:
        return self.newscategory

class news_detail(models.Model):
    newsposition=models.IntegerField(blank=True,null=True)
    othourname=models.CharField(max_length=50,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True )
    newscetegory=models.ForeignKey(category,on_delete=models.CASCADE ,blank=True,null=True)
    newsheador=models.CharField(max_length=300, blank=True,null=True)
    newscontent=HTMLField(blank=True,null=True)
    newsimg=models.ImageField(upload_to='img',blank=True,null=True)

    def __str__(self) -> str:
        return self.newsheador 

class comment(models.Model):
    post_id=models.ForeignKey(news_detail,on_delete=models.CASCADE,blank=True,null=True )
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True )
    name=models.CharField(max_length=50)
    email=models.EmailField()
    disc=models.TextField()

    def __str__(self) -> str:
        return self.name
   
    