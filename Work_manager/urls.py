from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'TaskManager.views.index.page', name="public_index"),
    url(r'^index$', 'TaskManager.views.index.page'),
    url(r'^connection$', 'TaskManager.views.connection.page', name="public_connection"),
)
