from django.conf.urls import url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'url_shrtnr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  
    url(r'^$',views.home,name='home'),
    url(r'^(?P<url>[-a-zA-Z0-9]+)/?$', views.short,name='short'),
]
