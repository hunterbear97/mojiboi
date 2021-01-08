from django.db import models

# Create your models here.
class Radical(models.Model):
    character = models.CharField(max_length=2)
    
    reading = models.ForeignKey('Sound', null=True, on_delete=models.CASCADE)
    
    meaning = models.ForeignKey('Meaning', null=True, on_delete=models.CASCADE)
    
    stroke_count = models.IntegerField()
    
    def __str__(self):
        return self.character
    
class Meaning(models.Model):
    meaning = models.CharField(max_length=50)
    
    def __str__(self):
        return self.meaning

class Sound(models.Model):
    romaji_sound = models.CharField(max_length=50)
    
    kana_sound = models.CharField(max_length=50)
    
    def __str__(self):
        return self.romaji_sound

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Kanji(models.Model):
    character = models.CharField(max_length=2)
    
    meanings = models.ManyToManyField(Meaning)
    
    readings = models.ManyToManyField(Sound)
    
    tags = models.ManyToManyField(Tag)
    
    stroke_count = models.IntegerField()
    
    
    
    