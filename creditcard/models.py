from django.db import models

"""
Models of credit card app for the Software Engineering Project
"""
class User(models.Model):
    """
    A simple user class
    @type user_name: String
    @param user_name:  username of user
    @type password: password 
    @param password: password of user
    @type verification_flag: boolean
    @param param: Verification flag whether user is verified or not
      
    Public functions:
    isPresent -- Checks whether user is present in our database and return true of false accordingly
    """
    user_name = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    verification_flag = models.CharField(max_length=20)
   
   

class PersonalDetail(models.Model):
    """
    
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    education = models.CharField(max_length=20)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    current_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    permanent_address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=13)
    mobile = models.CharField(max_length=13)
    user = models.OneToOneField(User)
 
class EmploymentDetail(models.Model):
    """
    
    """
    company_type = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    income = models.FloatField()
    work_years = models.IntegerField(max_length=2)
    name = models.CharField(max_length=200)
    office_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    email_id = models.CharField(max_length=50) 
    user = models.OneToOneField(User)
 
class BankDetail(models.Model):
    """
    
    """
    account_number = models.CharField(max_length=20)
    bankname = models.CharField(max_length=200)
    branch_address = models.CharField(max_length=200)
    account_type = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    
class Card(models.Model):
    """
    
    """
    card_number = models.CharField(max_length=200)
    card_type = models.CharField(max_length=200)	
    interest = models.FloatField()
    credited_amount = models.FloatField()
    user = models.OneToOneField(User)
   
class Statement(models.Model):
    """
    
    """
    transaction_date = models.DateTimeField('date of transaction')
    amount = models.FloatField()
    to_account = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length = 20)
    description = models.CharField(max_length= 100)    
    card = models.ForeignKey(Card)
   
