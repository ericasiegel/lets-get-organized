from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id', 'name']
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id', 'name']
        
        
class StorageType(models.Model):
    name = models.CharField(max_length=100)
    # StorageType can be in many Locations  
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='storage_type') 
    # Date & Time is updated as the database is updated
    date_organized = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id', 'name', 'date_organized']
    

class Object(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(max_length=500, null=True, blank=True)
    # Date & Time is updated as the database is updated
    last_updated = models.DateTimeField(auto_now=True) 
    # Object belongs to multiple Categories and a Category can have multiple Objects
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='objects', null=True) 
    # Multiple locations can be assigned to one object 
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='objects') 
    # A single storage type is specified
    storage_type = models.ForeignKey(StorageType, on_delete=models.PROTECT, null=True, blank=True, related_name='objects')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id', 'name', 'location', 'storage_type', 'last_updated']





# **** ADD the following if we want to add a DateTime field do the StorageType Field ****

#     locations = models.ManyToManyField(Location, through='StorageLocation') # to be added in place of the other Location field
    
#     # Intermediary model needed to be able to store additional information about the relationship between Location and StorageType
# class StorageLocation(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     storage_type = models.ForeignKey(StorageType, on_delete=models.CASCADE)