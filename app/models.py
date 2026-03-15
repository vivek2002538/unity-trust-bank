from django.db import models

# Create your models here.
class gender(models.Model):
    name=models.CharField(max_length=6)
    def __str__(self):
        return self.name

class account(models.Model):
    acc_num=models.AutoField(primary_key=True,default=1234567890)
    name=models.CharField(max_length=100)
    dob=models.DateField()
    aadhar=models.PositiveBigIntegerField(unique=True)
    pan=models.CharField(max_length=10,unique=True)
    phone=models.PositiveBigIntegerField(unique=10)
    gender=models.ForeignKey(gender,on_delete=models.CASCADE)
    pin=models.CharField(max_length=64)
    bal=models.IntegerField(default=1000)

class Transaction(models.Model):
    acc=models.ForeignKey(account,on_delete=models.CASCADE)
    transaction_type=models.CharField(max_length=20)
    amount=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.acc.acc_num}-{self.transaction_type}-{self.amount}'