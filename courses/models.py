from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100,blank = True,null =True)
    email = models.EmailField(unique=True,blank = True,null =True)
    phone = models.CharField(max_length=15,blank = True,null =True)
    expertise = models.CharField(max_length=100,blank = True,null =True)

    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    name = models.CharField(max_length=100,blank = True,null =True)
    description = models.TextField(blank = True,null =True)
    start_date = models.DateField(blank = True,null =True)
    end_date = models.DateField(blank = True,null =True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name