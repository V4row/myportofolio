import uuid

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

def validate_percentage(value):
    nilai = value
    if nilai < 0 or nilai > 100:
        message = "Persentase tidak valid"
        raise ValidationError(message)


class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
class Skill(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   title = models.CharField(max_length=255)
   percentage = models.IntegerField(default=0, validators=[validate_percentage])

   def __str__(self):
       return self.title
   
class Project(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   title = models.CharField(max_length=255)
   description = models.TextField()
   thumbnail = models.URLField(blank=True, null=True)
   url = models.URLField(blank=False, null=False)
   starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

   def __str__(self):
       return self.title