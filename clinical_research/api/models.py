from django.db import models

# Create your models here.
class Study(models.Model):
    title = models.CharField(max_length=255)
    therapeutics = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    condition = models.CharField(max_length=255)
    recruitment_date = models.DateField()
    study = models.ForeignKey(Study, related_name='patients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name