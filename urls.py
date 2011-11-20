from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
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
	(r'^creditcard/user/successtransfer.html$', 'creditcard.views.pay_to_account'),
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
