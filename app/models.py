from django.db import models
from django.utils import timezone

# Create your models here.
class operating_system(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Computer(models.Model):
    computer_name = models.CharField(max_length=20,blank=True,null=True)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    users_name = models.CharField(max_length=30,blank=True,null=True)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField("Purchase Date (mm/dd/yyyy)", auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    operating_system = models.ForeignKey(operating_system, on_delete=models.CASCADE,blank=True, null=True)
    

def __str__(self):
    return self.computer_name

