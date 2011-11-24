from djangorestframework.resources import ModelResource
from BankCreditCard.creditcard.models import User, Card, Statement, BankDetail, EmploymentDetail, PersonalDetail, Autopay

"""
#  Demonstrates API's input validation using form input
 bash: curl -X POST --data 'foo=true' http://api.django-rest-framework.org/model-resource-example/
 {"detail": {"bar": ["This field is required."], "baz": ["This field is required."]}}

 #  Demonstrates API's input validation using JSON input
 bash: curl -X POST -H 'Content-Type: application/json' --data-binary '{"foo":true}' http://api.django-rest-framework.org/model-resource-example/
{"detail": {"bar": ["This field is required."], "baz": ["This field is required."]}}
"""

class UserResource(ModelResource):
    model = User
    fields = ('user_name', 'password', 'verification_flag', 'url')

class PersonalDetailResource(ModelResource):
    model = PersonalDetail
    fields = ('first_name', 'last_name', 'gender', 'education', 'father_name', 'mother_name' , 'current_address', 'city', 'pincode', 'permanent_address', 'telephone', 'mobile', 'url')
    ordering = ('user',)
        
class EmploymentDetailResource(ModelResource):
    model = EmploymentDetail
    fields = ('company_type', 'designation', 'income', 'work_years', 'name', 'office_address', 'city', 'pincode', 'email_id' , 'user', 'url')
    ordering = ('user',)
    
class BankDetailResource(ModelResource):
    model = BankDetail
    fields = ('account_number', 'bankname', 'branch_address', 'account_type', 'user', 'url')
    ordering = ('user')

class CardResource(ModelResource):
    model = Card
    fields = ('card_number', 'card_type', 'interest', 'credited_amount', 'user', 'url')
    ordering = ('user',)    
    
class StatementResource(ModelResource):    
    model = Statement
    fields = ('transaction_date', 'amount', 'to_account', 'transaction_id', 'description', 'card', 'url')
    
class AutopayResource(ModelResource):
    model = Autopay
    fields = ('to_account', 'description', 'amount', 'date', 'installment', 'user', 'url')
    ordering = ('user')
