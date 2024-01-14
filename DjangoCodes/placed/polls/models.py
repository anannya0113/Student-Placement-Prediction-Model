from django.db import models

# Create your models here.
# class Userdb(models.Model):
#     email = models.CharField(max_length=100,null = True)
#     password = models.CharField(max_length=100,null = True)

#     class Meta:
#         db_table = 'login'


class Place(models.Model):
    Internship = models.CharField(max_length=100)
    CGPA = models.CharField(max_length=100)
    Hostel = models.CharField(max_length=100)
    HistoryOfBacklogs = models.CharField(max_length=100)


