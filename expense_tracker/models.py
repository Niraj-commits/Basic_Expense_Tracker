from django.db import models

# Create your models here.

class account(models.Model):
    
    track_types = [('Expense','Expense'),('Income','Income')]
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2,max_digits=500)
    addition_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50,choices=track_types,default="Income")
    

def __str__(self):
    return self.name
