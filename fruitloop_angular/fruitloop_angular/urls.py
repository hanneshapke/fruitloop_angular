from django.conf.urls import patterns, include, url
from django.contrib import admin

from fruit.views import FruitLocationCreateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', FruitLocationCreateView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
