from django.urls import path
from home.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]
