from __future__ import unicode_literals
from django.conf.urls import include, url, patterns
from django.contrib import admin
from web import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^blog/(?P<slug>[-\w]+)', views.blog_post, name='blog_post'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^members/form', views.member_form, name='member_form'),
    url(r'^members/apply', views.member_form_submit, name='member_form_submit'),
    url(r'^members/(?P<nickname>[-\w]+)', views.profile, name='profile'),
    url(r'^members/', views.members, name='members'),
    url(r'^kokdizin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^(?P<slug>[-\w]+)/', views.page, name='page'),
]