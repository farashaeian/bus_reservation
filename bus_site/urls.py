from django.conf.urls import url
from . import views

app_name='bus_site'
urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^search_reserv', views.search_reserv, name='search_reserv'),
    url(r'^reserv_report', views.reserv_report, name='reserv_report'),
    url(r'^cancel', views.cancel, name='cancel'),
]
