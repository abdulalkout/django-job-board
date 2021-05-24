from django.db import models

# Create your models here.
'''
django modle field
    - html widget
    - validation 
    - db size 

'''
class Job (models.Model) : # table
    title = models.CharField(max_length=100)  #coulmn