from uuid import uuid4
import os
from django.db import models


def post_image_path(instance, filename):
    """
    Generate path for post image using UUID to ensure uniqueness.
    """
    ext = os.path.splitext(filename)[1]
    return os.path.join('posts', f'{uuid4()}{ext}') 

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)

class Patient(models.Model):
    ssn = models.CharField(max_length=255, primary_key=True) # social security numbers
    name = models.CharField(max_length=255, db_index=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, db_index=True)

class Claim(models.Model):
    id = models.IntegerField(primary_key=True)
    ssn = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True ,db_index=True)
