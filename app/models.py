from django.db import models

# Create your models here.


class account(models.Model):
    acc_num=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    dob=models.DateField()
    aadhar=models.PositiveBigIntegerField(unique=True)
    pan=models.CharField(max_length=10,unique=True)
    phone=models.PositiveBigIntegerField(unique=True)
    gender=models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    pin=models.CharField(max_length=64)
    bal=models.IntegerField(default=1000)
    password=models.CharField(max_length=128)

class Transaction(models.Model):
    acc=models.ForeignKey(account,on_delete=models.CASCADE)
    transaction_type=models.CharField(max_length=20)
    amount=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.acc.acc_num}-{self.transaction_type}-{self.amount}'