from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    repository = models.URLField()
    skill = models.ManyToManyField('skill', related_name='projects')

    def __str__(self):
        return f'{self.name} - {self.year}'
    

class Experience(models.Model):
    entity = models.CharField(max_length=100)
    title = models.CharField(max_length=225)
    description = models.TextField()
    period = models.CharField(max_length=50)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f'{self.title} at {self.entity}'