from django.db import models


class Group(models.Model):
    number = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.number
    
    def create_slug(self):
        return f"{self.number}-group"

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Student(models.Model):
    group = models.ForeignKey(Group, related_name="students", on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.group.slug}/{self.id}/"
