from django.conf.urls import patterns, include, url
from django.contrib import admin

from fruit.views import FruitAPIList, FruitAPIDetail

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/$', FruitAPIList.as_view(), name='api_list'),
    url(r'^api/(?P<pk>[0-9]+)/$', FruitAPIDetail.as_view(), name='api_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
