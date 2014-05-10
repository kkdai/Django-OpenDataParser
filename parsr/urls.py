from django.conf.urls import patterns, include, url
from django.contrib import admin
#from parsr import views
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post_doc', views.parse, name='index'),
    url(r'^xml', views.xml, name='index'),
    url(r'^post_xml', views.xmlparse, name='index'),
    #url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
