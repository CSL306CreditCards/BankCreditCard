from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^creditcard/register$', 'creditcard.views.register'),
	(r'^creditcard/register/success/$', 'creditcard.views.process'),
	(r'^creditcard/home/$', 'creditcard.views.index'),
	(r'^creditcard/home/cards.html$', 'creditcard.views.cards'),
	(r'^creditcard/home/index.html$', 'creditcard.views.index'),
	(r'^creditcard/home/services.html$', 'creditcard.views.services'),
	(r'^creditcard/home/contact-us.html$', 'creditcard.views.contact'),
	(r'^creditcard/home/sitemap.html$', 'creditcard.views.sitemap'),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static',
(r'^creditcard/home/(?P<path>.*)$',
	'serve', {
	'document_root': 'static',
		'show_indexes': True}),)