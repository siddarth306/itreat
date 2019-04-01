
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

app_name='ModelApplication'
## loof for cross site request forgery
urlpatterns = [
    url(r'^create/$', views.createJob, name='create'),

]
