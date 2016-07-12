from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from todos import views, todoclassviews
from django.contrib.auth import views as authviews
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^todolists',login_required(views.display_lists,login_url='/login/'),name='todolist'),
    url(r'^createlist/',todoclassviews.CreateToDoListView.as_view(),name='todolistcreate'),
    url(r'^custom/',views.createlist,name='customlistcreate'),
    url(r'^deletelist/(?P<pk>[0-9]+)',todoclassviews.DeleteToDoListView.as_view(),name='todolistcreate'),
    url(r'^updatelist/(?P<pk>[0-9]+)',todoclassviews.UpdateToDoListView.as_view(),name='todolistcreate'),
    url(r'createitem/(?P<pk>[0-9]+)',todoclassviews.CreateToDoItemView.as_view(),name='todoitemcreate'),
    url(r'deleteitem/(?P<pk>[0-9]+)',todoclassviews.DeleteToDoItemView.as_view(),name='todoitemdelete'),
    url(r'updateitem/(?P<pk>[0-9]+)',todoclassviews.UpdateToDoItemView.as_view(),name='todoitemupdate'),
]