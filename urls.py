from django.conf.urls.defaults import patterns, include, url
#from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
#from BankCreditCard.creditcard.models import User, Card, Statement, BankDetail, EmploymentDetail, PersonalDetail, Autopay
from BankCreditCard.creditcard.resources import UserResource, CardResource, StatementResource, BankDetailResource, EmploymentDetailResource, PersonalDetailResource, AutopayResource
from django.contrib import admin
admin.autodiscover()
   
urlpatterns = patterns('',
    url(r'^creditcard/api/user$', ListOrCreateModelView.as_view(resource=UserResource), name='model-resource-User'),
    url(r'^creditcard/api/user/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=UserResource)),
    url(r'^creditcard/api/personaldetail$', ListOrCreateModelView.as_view(resource=PersonalDetailResource), name='model-resource-PersonalDetail'),
    url(r'^creditcard/api/personaldetail/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=PersonalDetailResource)),
    url(r'^creditcard/api/employmentdetail$', ListOrCreateModelView.as_view(resource=EmploymentDetailResource), name='model-resource-EmploymentDetails'),
    url(r'^creditcard/api/employmentdetail/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=EmploymentDetailResource)),
    url(r'^creditcard/api/bankdetail$', ListOrCreateModelView.as_view(resource=BankDetailResource), name='model-resource-BankDetails'),
    url(r'^creditcard/api/bankdetail/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=BankDetailResource)),
    url(r'^creditcard/api/card$', ListOrCreateModelView.as_view(resource=CardResource), name='model-resource-Card'),
    url(r'^creditcard/api/card/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=CardResource)),
    url(r'^creditcard/api/statement$', ListOrCreateModelView.as_view(resource=StatementResource), name='model-resource-Statement'),
    url(r'^creditcard/api/statement/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=StatementResource)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^creditcard/api/autopay$', ListOrCreateModelView.as_view(resource=AutopayResource), name='model-resource-Autopay'),
    url(r'^creditcard/api/autopay/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=AutopayResource)),
<<<<<<< HEAD
    url(r'^creditcard/api/payment_api.html/account_no=(?P<account_no>\d+)/amount=(?P<amount>\d+)/$', 'creditcard.views.paymentApi'),
    url(r'^creditcard/api/successpayment_api.html/(?P<account_no>\d+)/(?P<amount>\d+)/$', 'creditcard.views.successpaymentApi'),
    url(r'^creditcard/home/$', 'creditcard.views.index'),
    url(r'^creditcard/home/index.html$', 'creditcard.views.index'),
	url(r'^creditcard/home/userDoesNotExist/$', 'creditcard.views.userDoesNotExist'),
	url(r'^creditcard/home/cards.html$', 'creditcard.views.cards'),
    url(r'^creditcard/home/services.html$', 'creditcard.views.services'),
	url(r'^creditcard/home/contactus.html$', 'creditcard.views.contact'),
    url(r'^creditcard/home/platinum.html$', 'creditcard.views.platinum'),
    url(r'^creditcard/home/gold.html$', 'creditcard.views.gold'),
    url(r'^creditcard/home/silver.html$', 'creditcard.views.silver'),
	url(r'^creditcard/home/sitemap.html$', 'creditcard.views.sitemap'),
	url(r'^creditcard/register$', 'creditcard.views.register'),
	url(r'^creditcard/register/userNameExistError/$', 'creditcard.views.userNameExistError'),
	url(r'^creditcard/home/registeredSuccessfully/$', 'creditcard.views.registeredSuccessfully'),
	url(r'^creditcard/register/success/$', 'creditcard.views.registerprocess'),
	url(r'^creditcard/user/$', 'creditcard.views.login'),
	url(r'^creditcard/user/index.html$', 'creditcard.views.userindex'),
	url(r'^creditcard/user/profile.html$', 'creditcard.views.userprofile'),
	url(r'^creditcard/user/statement.html$', 'creditcard.views.userstatement'),
	url(r'^creditcard/user/transfer.html$', 'creditcard.views.usertransfer'),
    url(r'^creditcard/user/services.html$', 'creditcard.views.userservices'),
    url(r'^creditcard/user/successautopay.html$', 'creditcard.views.autopay'),
    url(r'^creditcard/user/removeautopay.html/remove_id=(?P<remove_id>\d+)$', 'creditcard.views.removeAutopay'),
	url(r'^creditcard/user/successtransfer.html$', 'creditcard.views.userPayToAccount'),
	url(r'^creditcard/user/successstatement.html$', 'creditcard.views.displayStatement'),
    url(r'^creditcard/user/paybill.html$', 'creditcard.views.payBill'),
    url(r'^creditcard/user/logout.html$', 'creditcard.views.logout'),
	url(r'^creditcard/sms_api/number=(?P<number>\d+)/message=(?P<message>.+)', 'creditcard.views.sendSms'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
)
urlpatterns += patterns('django.views.static',
    (r'^creditcard/api/(?P<path>.*)$', 'serve', {'document_root': 'static'}),

)
urlpatterns += patterns('django.views.static',
	(r'^creditcard/home/(?P<path>.*)$', 'serve', {'document_root': 'static'}),
)

urlpatterns += patterns('django.views.static',
	(r'^creditcard/user/(?P<path>.*)$', 'serve', {'document_root': 'static'}),
)
urlpatterns += patterns('django.views.static',
    (r'^(?P<path>.*)$', 'serve', {'document_root': 'static'}),
)
