from django.conf.urls import patterns, include, url

urlpatterns = patterns('villagalde.apps.home.views',
    url(r'^$','index_view', name='vista_principal'),
)