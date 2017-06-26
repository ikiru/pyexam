from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.create),
    url(r'^success$', views.success),
    url(r'^result$', views.result),
    url(r'^logout$', views.logout),

    ]
