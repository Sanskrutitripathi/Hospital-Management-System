from datetime import time
import uuid
from django.db import models

# Create your models here.
class appointment(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, unique=True, default=uuid.uuid4, max_length=50)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6)
    date = models.DateField()
    time = models.TimeField(unique_for_date=True)
    doc_name = models.CharField(max_length=60, default='')
    doc_id = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        name = f"{self.fname} {self.lname}"
        return name
    
class doctor(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, unique=True, default=uuid.uuid4, max_length=50)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    experience = models.PositiveIntegerField()
    speciality = models.CharField(max_length=50)

    def __str__(self) -> str:
        name = f"{self.fname} {self.lname} - ({self.speciality})"
        return name
    
class patient(models.Model):
    pid = models.UUIDField(auto_created=True, primary_key=True, unique=True, default=uuid.uuid4, max_length=50)
    name = models.CharField(max_length=60, default='')
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6)
    doc_id = models.CharField(max_length=50, default='')
    
    def __str__(self) -> str:
        name = self.name
        return name

class staff(models.Model):
    sid = models.UUIDField(auto_created=True, primary_key=True, unique=True, default=uuid.uuid4, max_length=50)
    name = models.CharField(max_length=60, default='')
    mobile = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6)
    role = models.CharField(max_length=30)

    def __str__(self) -> str:
        name = f"{self.name} ({self.role})"
        return name

class historie(models.Model):
    pid = models.UUIDField(auto_created=True, primary_key=True, unique=True, default='', max_length=50)
    name = models.CharField(max_length=60, default='')
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6)
    doc_id = models.CharField(max_length=50, default='')
    doc_name = models.CharField(max_length=50, default='')
    doc_spec = models.CharField(max_length=50, default='')
    
    def __str__(self) -> str:
        name = self.name
        return name
