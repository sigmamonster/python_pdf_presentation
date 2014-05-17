from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('main.views',
    url(r'^print-to-pdf/(?P<name>[^/]*)/(?P<url>.*)$',
        'print_to_pdf', name='print_to_pdf'),
)
