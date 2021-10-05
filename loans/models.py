from django.db import models
from accounts.models import User
# Create your models here.

class Loan_Template(models.Model):
    type= models.CharField(max_length=1)
    interest_rate= models.FloatField()
    start= models.IntegerField()
    end= models.IntegerField()

    def __str__(self):
        return self.type


class Loan1(models.Model):
    #foreign key with type
    amount= models.FloatField()
    type= models.ForeignKey(Loan_Template, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()



class Loan_Fund(models.Model):
    #foreign key with type
    amount= models.FloatField()
    type= models.ForeignKey(Loan_Template, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()
