from django.conf.urls.defaults import patterns, include, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from BankCreditCard.creditcard.models import *
from BankCreditCard.creditcard.resources import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#class User(ModelResource):
#    model = User
    
urlpatterns = patterns('',
    url(r'^creditcard/api/user$',ListOrCreateModelView.as_view(resource=UserResource), name='model-resource-User'),
    url(r'^creditcard/api/user/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=UserResource)),
    url(r'^creditcard/api/personaldetail$',ListOrCreateModelView.as_view(resource=PersonalDetailResource), name='model-resource-PersonalDetail'),
    url(r'^creditcard/api/personaldetail/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=PersonalDetailResource)),
    url(r'^creditcard/api/employmentdetail$',ListOrCreateModelView.as_view(resource=EmploymentDetailResource), name='model-resource-EmploymentDetails'),
    url(r'^creditcard/api/employmentdetail/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=EmploymentDetailResource)),
    url(r'^creditcard/api/bankdetail$',ListOrCreateModelView.as_view(resource=BankDetailResource), name='model-resource-BankDetails'),
    url(r'^creditcard/api/bankdetail/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=BankDetailResource)),
    url(r'^creditcard/api/card$',ListOrCreateModelView.as_view(resource=CardResource), name='model-resource-Card'),
    url(r'^creditcard/api/card/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=CardResource)),
    url(r'^creditcard/api/statement$',ListOrCreateModelView.as_view(resource=StatementResource), name='model-resource-Statement'),
    url(r'^creditcard/api/statement/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=StatementResource)),
    url(r'^creditcard/api/autopay$',ListOrCreateModelView.as_view(resource=AutopayResource), name='model-resource-Autopay'),
    url(r'^creditcard/api/autopay/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=AutopayResource)),
    
    
    
    (r'^creditcard/api/payment_api.html/account_no=(?P<account_no>\d+)/amount=(?P<amount>\d+)/$', 'creditcard.views.payment_api'),
    (r'^creditcard/api/successpayment_api.html/(?P<account_no>\d+)/(?P<amount>\d+)/$', 'creditcard.views.successpayment_api'),
    (r'^creditcard/home/$', 'creditcard.views.index'),
    (r'^creditcard/home/index.html$', 'creditcard.views.index'),
	(r'^creditcard/home/userDoesNotExist/$', 'creditcard.views.userDoesNotExistIndex'),
	(r'^creditcard/home/cards.html$', 'creditcard.views.cards'),
    (r'^creditcard/home/services.html$', 'creditcard.views.services'),
	(r'^creditcard/home/contactus.html$', 'creditcard.views.contact'),
    (r'^creditcard/home/platinum.html$', 'creditcard.views.platinum'),
    (r'^creditcard/home/gold.html$', 'creditcard.views.gold'),
    (r'^creditcard/home/silver.html$', 'creditcard.views.silver'),
	(r'^creditcard/home/sitemap.html$', 'creditcard.views.sitemap'),
	(r'^creditcard/register$', 'creditcard.views.register'),
	(r'^creditcard/register/userNameExistError/$', 'creditcard.views.userNameExistError'),
	(r'^creditcard/home/registeredSuccessfully/$', 'creditcard.views.registeredSuccessfully'),
	(r'^creditcard/register/success/$', 'creditcard.views.registerprocess'),
	(r'^creditcard/user/$', 'creditcard.views.login'),
	(r'^creditcard/user/index.html$', 'creditcard.views.userindex'),
	(r'^creditcard/user/profile.html$', 'creditcard.views.userprofile'),
	(r'^creditcard/user/statement.html$', 'creditcard.views.userstatement'),
	(r'^creditcard/user/transfer.html$', 'creditcard.views.usertransfer'),
    (r'^creditcard/user/services.html$', 'creditcard.views.userservices'),
    (r'^creditcard/user/successautopay.html$', 'creditcard.views.autopay'),
    (r'^creditcard/user/removeautopay.html/remove_id=(?P<remove_id>\d+)$', 'creditcard.views.removeautopay'),
	(r'^creditcard/user/successtransfer.html$', 'creditcard.views.user_pay_to_account'),
	(r'^creditcard/user/successstatement.html$', 'creditcard.views.display_statement'),
    (r'^creditcard/user/logout.html$', 'creditcard.views.logout'),
	(r'^creditcard/sms_api/number=(?P<number>\d+)/message=(?P<message>.+)', 'creditcard.views.send_sms'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
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
