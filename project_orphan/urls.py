from django.conf.urls import url
from django.contrib import admin

from accounts import views as accounts_views
from orphan import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
]
