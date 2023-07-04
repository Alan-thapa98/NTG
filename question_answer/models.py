from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.core.validators import FileExtensionValidator
from profiles.models import Profile
# Create your views here.

# which class they are reading.


class which_author(models.Model):
    author = models.CharField(max_length=255)
    bio = models.TextField(max_length=5000)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.author


class which_type(models.Model):
    types = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.types


class which_grade (models.Model):
    grade = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.grade


class which_language(models.Model):
    language = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.language


class which_subject(models.Model):
    subject = models.CharField(max_length=255)
    image = models.ImageField(default='bg.png', upload_to='avatars/')
    bio = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.subject



class which_subject_category(models.Model):
    subject_category = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.subject_category


# answer question, quiz,different between,quiz, Full forms, different between
class answer_question(models.Model):
    sno = models.AutoField(primary_key=True)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='answer_question')
    author = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.TextField(max_length=5555)
    types = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
   
    subject_category = models.CharField(max_length=255)
    
    slug = AutoSlugField(populate_from='question',
                         unique=True, null=False, default=False)
    
    stars = models.IntegerField(default=1)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " Question: " + self.question + " by " + self.author + " " + self.grade


