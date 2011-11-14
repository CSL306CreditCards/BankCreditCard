from creditcard.models import User
from creditcard.models import PersonalDetail
from creditcard.models import EmploymentDetail
from creditcard.models import BankDetail
from creditcard.models import Statement
from creditcard.models import Card
from django.contrib import admin

admin.site.register(User)
admin.site.register(PersonalDetail)
admin.site.register(EmploymentDetail)
admin.site.register(BankDetail)
admin.site.register(Statement)
admin.site.register(Card)