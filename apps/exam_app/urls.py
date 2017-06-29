from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^add$', views.add),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^(?P<id>\d+)/$', views.result),
    url(r'^dash$', views.dash),
    url(r'^add_trip$', views.add_trip),
]
#(?<id>\d+)/$
#{% url 'result id=object.id '%}
