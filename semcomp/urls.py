from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from palestras.views import hello_world, lista_palestras


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'semcomp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello-world$', hello_world),
    url(r'^palestras$', lista_palestras),
)
