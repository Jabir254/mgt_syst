from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField(primary_key = True)
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
    password = models.CharField(max_length=10)
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
    
class teacher(models.model):
    teacher_id = models.AutoField(primary_key = True)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_joined_school = models.DateField()
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class attendace(models.Model):
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher',on_delete=models.CASCADE )
    date = models.DateField.auto_now()
    STATUS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

    def __str__(self):
         return f'{self.user_id} - {self.date}'
