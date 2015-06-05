from django.conf.urls import include, url
from django.contrib import admin
from .views import home, home_files

urlpatterns = [
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home, name="home"),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name="home_files"),

    url(r'^admin/', include(admin.site.urls)),
]
