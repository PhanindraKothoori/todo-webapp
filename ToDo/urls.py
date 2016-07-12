"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin

import todos
from todos import api, views, todoclassviews
from django.contrib.auth import views,urls

urlpatterns = [

    #TODO - add the respective views to registration
    url(r'^logout/',todos.views.logoutuser,name='logout'),
    url(r'^signup/$', todoclassviews.UserformView.as_view(), name='signup'),
    url(r'^',include(urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^todo/', include('todos.urls')),
    url(r'^api/listall/$',api.ToDoListAll),
    url(r'^api/listall/(?P<pk>[0-9]+)/$',  api.ToDoListOne),
    url(r'^api/listall/(?P<pk>[0-9]+)/listitems/$', api.ToDoItemsAll),
    url(r'^api/listall/(?P<pklist>[0-9]+)/listitems/(?P<pkitem>[0-9]+)/$', api.ToDoItemOne),
]
