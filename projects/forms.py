from ast import Import
from dataclasses import fields
from http.client import ImproperConnectionState
from logging import PlaceHolder
from pyexpat import model
from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'Tags']

        # Changed Tags to checbox on the page (module import: from django import form den import widgets from django.form)
        widgets= {
            'Tags': forms.CheckboxSelectMultiple(),
        }
    
    # below code use to override default STYLES and assign CSS class to fields
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        #______________doing it one by one will make this code messy so lets iterate over the fields
        #self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Enter Title'})
        #self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Enter Title'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        
        labels = {
        'value' : 'Place your vote',
        'body' : 'Add a comment with Your Vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})