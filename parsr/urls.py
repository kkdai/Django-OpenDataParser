from django.conf.urls import patterns, include, url
from django.contrib import admin
#from parsr import views
import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^post_doc', views.parse, name='index'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
