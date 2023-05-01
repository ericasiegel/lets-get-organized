from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    
    
class StorageType(models.Model):
    name = models.CharField(max_length=100)
    # StorageType can be in many Locations  
    locations = models.ManyToManyField(Location)
    # Date & Time is updated as the database is updated
    date_organized = models.DateTimeField(auto_now=True)
    

class Object(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField(max_length=500, null=True, blank=True)
    # Date & Time is updated as the database is updated
    last_updated = models.DateTimeField(auto_now=True) 
    # Object belongs to multiple Categories and a Category can have multiple Objects
    category = models.ManyToManyField(Category) 
    # Multiple locations can be assigned to one object 
    locations = models.ManyToManyField(Location) 
    # A single storage type is specified
    storage_type = models.ForeignKey(StorageType, on_delete=models.CASCADE)

    
# **** ADD the following if we want to add a DateTime field do the StorageType Field ****

#     locations = models.ManyToManyField(Location, through='StorageLocation') # to be added in place of the other Location field
    
#     # Intermediary model needed to be able to store additional information about the relationship between Location and StorageType
# class StorageLocation(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     storage_type = models.ForeignKey(StorageType, on_delete=models.CASCADE)