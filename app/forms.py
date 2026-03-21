from django import forms
from .models import account

class Registration_form(forms.ModelForm):
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    gender=forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model=account
        fields=['name','dob','aadhar','pan','phone','gender']

class pin_validation(forms.Form):
    account_num=forms.IntegerField()
    aadhar=forms.IntegerField()
    pin=forms.IntegerField()
    c_pin=forms.IntegerField()