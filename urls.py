from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^creditcard/home/$', 'creditcard.views.index'),
	(r'^creditcard/home/cards.html$', 'creditcard.views.cards'),
	(r'^creditcard/home/index.html$', 'creditcard.views.index'),
	(r'^creditcard/home/services.html$', 'creditcard.views.services'),
	(r'^creditcard/home/contact-us.html$', 'creditcard.views.contact'),
	(r'^creditcard/register$', 'creditcard.views.register'),
	(r'^creditcard/home/sitemap.html$', 'creditcard.views.sitemap'),
	(r'^creditcard/register/success/$', 'creditcard.views.process'),
	(r'^creditcard/user/$', 'creditcard.views.login'),
	(r'^creditcard/user/index.html$', 'creditcard.views.userindex'),
	(r'^creditcard/user/profile.html$', 'creditcard.views.userprofile'),
	(r'^creditcard/user/statement.html$', 'creditcard.views.userstatement'),
	(r'^creditcard/user/transfer.html$', 'creditcard.views.usertransfer'),
	(r'^creditcard/user/successtransfer.html$', 'creditcard.views.pay_to_account'),
	(r'^creditcard/user/successstatement.html$', 'creditcard.views.display_statement'),
	url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('django.views.static',
	(r'^creditcard/home/(?P<path>.*)$', 'serve', {'document_root': 'static'}),
)

urlpatterns += patterns('django.views.static',
	(r'^creditcard/user/(?P<path>.*)$', 'serve', {'document_root': 'static'}),
)
