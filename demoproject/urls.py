from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', "demoapp.views.homepage"),
    (r'^comments/', include('django.contrib.comments.urls')),
)