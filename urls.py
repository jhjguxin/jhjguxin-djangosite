#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#from mysite.views import hello, my_homepage_view,current_datetime,hours_ahead,display_meta
from mysite import views
from mysite.books import views#from mysite.books.views import search_form
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from mysite.books.models import Publisher,Book
from django.conf.urls.defaults import *
from mysite.feeds.feeds import LatesEntries
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.auth.views import login,logout
#global urlpatterns
urlpatterns = patterns('mysite.views',
#    (r'^admin/',include(admin.site.urls)),
    (r'^hello1/$', 'hello1'),
    (r'^$', 'my_homepage_view',),
    (r'^hello/$', 'hello'),
    (r'^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'),#'\'转义
    (r'^request_info/$','display_meta'),
    (r'^about/(\w+)$','about_pages'),#if page is not exsites return 404 error
    (r'^Firefox_wallpaper/$','my_image'),
    (r'^unruly_passengers_csv/$','unruly_passengers_csv'),
    (r'^register/$','register'),
    (r'^aboutme/Personal_Details.txt','Personal_Details'),
    (r'^aboutme/$','aboutme'),

)
#def get_book():
#  return Book.objects.all()

publisher_info={
    'queryset':Publisher.objects.all(),
    'template_name':'publisher_list_page.html',
    'template_object_name':'Publisher',
#    'extra_context': {'book_list': Book.objects.all()}
#    'extra_context': {'book_list':get_books}
    'extra_context': {'book_list':Book.objects.all},#注意 Book.objects.all  后面没有括号；这表示这是一个函数的引用，并没有 真调用它
}
book_info={
    'queryset':Book.objects.order_by('-publication_date'),
    'template_name':'book_list.html',
    'template_object_name':'book',
}
apress_books={
    'queryset':Book.objects.filter(publisher__name="O'Reilly"),
    'template_name':'apress_list.html',
    'template_object_name':'apress',
}

feeds={
    'latest':LatesEntries,
#    'categories':LatestEntriesByCategory,
}
#////////////////////////
info_dict = {
    'queryset': Book.objects.all(),
    'date_field': 'publication_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'books': GenericSitemap(info_dict, priority=0.6),
}


#/////////////////////
urlpatterns += patterns('',
    (r'^admin/',include(admin.site.urls)),
    (r'^about/$',direct_to_template,{'template':'about.html'}),  
    (r'^publishers/$',list_detail.object_list,publisher_info),
    (r'^books/$',list_detail.object_list,book_info),
    (r'^books/apress$',list_detail.object_list,apress_books),
#    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/media'}),
    (r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),#feeds 登入使用地址feeds/latest
#    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+).xml$','django.contrib.sitemaps.views.sitemap',{'sitemaps': sitemaps}),

    (r'^sitemap.xml$','django.contrib.sitemaps.views.index',{'sitemaps': sitemaps}),
    (r'^login',login,{"template_name":'login.html'}),
    (r'^logout/$', logout),

    

)
urlpatterns+=patterns('mysite.books.views',
    (r'^search-form/$','search_form'),
    (r'^search/$','search'),
    #(r'^contact-form/$',views.contact),
    (r'^contact/$','contact'),
    (r'^contact/thanks/$','thanks'),
    (r"^books/([\w'\s]+)$",'books_by_publisher'),
    (r"^authors/(?P<author_id>\d+)/$",'author_detail'),
   # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
        (r'^map/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'map'}),
    )

