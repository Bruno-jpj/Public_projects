from django.db import models
from django.utils.text import slugify
# Create your models here.

# modello dei siti
class Site(models.Model):
    CATEGORY_CHOICES = [
        #('valore salvato nel db lato server','valore mostrato a video lato client')
        ('ChatBot','ChatBot'),
        ('TextToImage','Text-To-Image'),
        ('TextToVideo','Text-To-Video'),
        ('Info','Info'),
        ('TextToAudio','Text-To-Audio'),
        ('SpeechToText','Speech-To-Text'),
        ('PromptGenerator','Prompt-Generator'),
        ('EditorEditing','Editor-Editing'),
        ('Animation3D','Animation3D'),
        ('Presentation','Presentation'),
        ('Analyses','Analyses'),
        ('Copywriting','Copywriting'),
        ('AppCreator','AppCreator'),
        ('Management','Management'),
        ('ContentIdeas','ContentIdeas'),
        ('ImageEnhancer', 'Image Enhancer'),  
        ('VideoEnhancer', 'Video Enhancer'),  
        ('Translation', 'Translation'), 
        ('CodeGenerator', 'Code Generator'),  
        ('DataAnalysis', 'Data Analysis'),  
        ('Marketing', 'Marketing Tools'), 
        ('SocialMedia', 'Social Media'),  
        ('EmailAssistant', 'Email Assistant'), 
        ('ResumeTools', 'Resume Tools'), 
        ('Education', 'Education'),  
        ('GameDev', 'Game Development'), 
        ('Productivity', 'Productivity'), 
        ('Security', 'Security'),  
        ('Finance', 'Finance & Investing'), 
        ('Legal', 'Legal Assistance'),
    ]
    # è una list comprehension che serve a pulire la lista/dizionario CATEGORY_CHOICES, rimuovendo eventuali tuple vuote o incomplete.
    CATEGORY_CHOICES = [ c for c in CATEGORY_CHOICES if all(c)] 
    #
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
    paid = models.BooleanField(default=False)
    url = models.URLField(max_length=256)
    #
    slug = models.SlugField(unique=True, blank=True) # creo il campo slug
    #
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # creo lo slug del titolo
        super().save(*args, **kwargs)
    #
    def __str__(self):
        return self.title
    
# modello degli User
class User(models.Model):
    Username = models.CharField(max_length=64, unique=True)
    Password = models.CharField(max_length=255)
    Email = models.CharField(max_length=64)
    #
    # rappresentazione testuale di un oggetto User
    def __str__(self):
        return self.Username
    #
#