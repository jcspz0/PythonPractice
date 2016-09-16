from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.landing),
    #url(r'^([0-9]{4})/$',
    #	views.year_archive),
    #url(r'^([0-9]{4})/([0-9]{2})/$',
    #	views.month_archive),
    #url(r'^([0-9]{4})/([0-9]{2})/([-a-z0-9]+)/$',
    #	views.year_archive),
]