from django.db import models
from accounts.models import User
# Create your models here.

class Loan_Template(models.Model):
    type= models.CharField(max_length=1)
    interest_rate= models.FloatField()
    start= models.IntegerField()
    end= models.IntegerField()
    payments_number= models.IntegerField()

    def __str__(self):
        return self.type


class Loan1(models.Model):
    #foreign key with type
    amount= models.FloatField()
    type= models.ForeignKey(Loan_Template, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()
    taken=models.BooleanField()
    #taken_by_user= models.ForeignKey(User, on_delete=models.CASCADE)



class Loan_Fund(models.Model):
    #foreign key with type
    amount= models.FloatField()
    type= models.ForeignKey(Loan_Template, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()
    taken=models.BooleanField()
    #taken_by_user= models.ForeignKey(User, on_delete=models.CASCADE)


class Loan_to_Loan_Fund(models.Model):
    loan = models.ForeignKey(Loan1, on_delete=models.CASCADE)
    loan_fund = models.ForeignKey(Loan_Fund, on_delete=models.CASCADE)
    
    pmt_out=models.FloatField(null=True, blank=True)
    class Meta:
        unique_together = [['loan', 'loan_fund']]