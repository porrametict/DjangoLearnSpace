from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def __str__(self):
        return self.user.username
