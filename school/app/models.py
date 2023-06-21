from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    date_joined_school = models.DateField()
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    parent_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'