from BankCreditCard.creditcard.models import User, Card, Statement, BankDetail, EmploymentDetail, PersonalDetail, Autopay
from django.contrib import admin

admin.site.register(User)
admin.site.register(PersonalDetail)
admin.site.register(EmploymentDetail)
admin.site.register(BankDetail)
admin.site.register(Statement)
admin.site.register(Card)
admin.site.register(Autopay)