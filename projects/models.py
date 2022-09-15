from enum import unique
from tkinter import FLAT
from django.db import models
import uuid
from users.models import Profile


class Project(models.Model): 
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    Tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    

    # the below meta class is used to arrange projects in assending or Descending (['-created']) Order
    class Meta:
        ordering = ['-vote_ratio', '-vote_total'] #this will make top rated project to be at d top



    @property    # this will return all Id of people that write review
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset   
 


    @property   #this we make us to run it as an attribute not as am actual method
    def getvoteCount(self):
        reviews =self.review_set.all() #Get all the Reviews
        upvotes = reviews.filter(value='up').count() 
        totalvotes = reviews.count() 

        ratio = (upvotes/totalvotes) * 100
        
        self.vote_total = totalvotes
        self.vote_ratio = ratio

        self.save()
        

class Review(models.Model):
    VOTE_TYPE = (
        ('Up', 'Up Vote'),
        ('Down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    class Meta:
        unique_together = [['owner', 'project']]

        
    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name