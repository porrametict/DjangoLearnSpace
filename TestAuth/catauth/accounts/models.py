from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


# Create your models here.
def has_perm(perm, obj=None):
    return True


class Admin(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, default='user')
    email = models.EmailField(
        verbose_name=' email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.email


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    object = UserManager()



class User(AbstractBaseUser):
    pass


class Teacher(AbstractBaseUser):
    pass


class Subject(models.Model):
    name = models.CharField(max_length=200)
    t_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Score(models.Model):
    name = models.CharField(max_length=200)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sj_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
