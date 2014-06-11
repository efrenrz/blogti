from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('villagalde.apps.home.urls')),
    url(r'^blog/', include('villagalde.apps.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
