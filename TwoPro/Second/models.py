from django.db import models

class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):

    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    date=models.DateField()

    def __str__(self):
        return str(self.date)
