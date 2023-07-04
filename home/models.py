from django.db import models

# Create your models here.


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    content = models.TextField(max_length=500)

    def __str__(self):
        return "Sir Alan, you have feedback by the name of " + self.name + " with email of " + self.email + ". Comment: " + self.content

    # facebook = models.TextField(max_length=9000)
    # twitter = models.TextField(max_length=9000)
    # instagram = models.TextField(max_length=9000)
    # youtube = models.TextField(max_length=9000)
