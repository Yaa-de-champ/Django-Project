from django.db import models
from django.contrib.auth.models import User
# from django.db.models.deletion import CASCADE

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-updated', '-created'] #order in ascending order

    def __str__(self):
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

# ----------------------------------------------------------------------------------------------------------------------------------
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'