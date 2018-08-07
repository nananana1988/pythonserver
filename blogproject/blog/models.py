#  coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


class Category (models.Model):
	"""docstring for Category """
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	"""docstring for Tag"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class  Post(models.Model):
	"""docstring for  Post"""
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200,blank=True)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User)
	def  get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})	
 
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-created_time','title']
		
		
		

# Create your models here.
