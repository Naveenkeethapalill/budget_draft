from django.db import models

class income(models.Model):
    iteam = models.CharField(max_length=20)
    amount = models.IntegerField(max_length=10000)
    date =   models.DateField()
    def __str__(self):
        return "{}-{}".format(self.iteam, self.amount) 
    
class expense(models.Model):
    iteam = models.CharField(max_length=20)
    amount = models.IntegerField(max_length=10000)
    date = models.DateField()
    def __str__(self):
        return "{}-{}".format(self.iteam, self.amount) 
    



