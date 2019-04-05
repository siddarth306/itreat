
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

app_name='homepage'
## loof for cross site request forgery
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^graphs$', views.graphs, name='graphs'),
    

]
