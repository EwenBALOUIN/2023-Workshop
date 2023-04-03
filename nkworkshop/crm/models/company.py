from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contacts = models.ManyToManyField('Customer', blank=True, related_name='companies')

    def __str__(self):
        return self.name
    
    def __plural__(self):
        return 'Companies'