from django.db import models

# Create your models here.

class Kana(models.Model):
    character = models.CharField(max_length=2)
    sound = models.ForeignKey('Sound', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.character

class Sound(models.Model):
    romaji = models.CharField(max_length=3)
    
    def __str__(self):
        return self.romaji

class Type(models.Model):
    name = models.CharField(max_length=8)
    
    def __str__(self):
        return self.name
