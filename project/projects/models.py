from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)


    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Category")


    def __str__(self):
        return self.name


class ProjectStatus(models.IntegerChoices):

    PENDING = 1,'pending'
    COMPLETED = 2,'completed'
    POSTPONED = 3,'postponed'
    CANCELED = 4,'canceled'
    




class Project(models.Model):

    titel = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField(choices=ProjectStatus.choices , default=ProjectStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE , null=True)

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.titel



class Task(models.Model):

    description = models.TextField()
    us_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.description

