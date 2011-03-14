#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#views.py
from django.template import Template,Context,TemplateDoesNotExist
from django.template.loader import get_template as get_Template
#我们不再需要导入 get_template  、 Template 、 Context 和 HttpResponse 。相反，我们导入 django.shortcuts.render_to_response
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from django.views.generic.simple import direct_to_template
import datetime



def hello(request):
  return HttpResponse("Hello world!")

def my_homepage_view(request):
  url="""
urlpatterns = patterns('mysite.views',
#    (r'^admin/',include(admin.site.urls)),
    (r'^hello1/$', 'hello1'),
    (r'^$', 'my_homepage_view'),
    (r'^hello/$', 'hello'),
    (r'^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'),#'\'转义
    (r'^request_info/$','display_meta'),
    (r'^about/(\w+)$','about_pages'),
)

urlpatterns += patterns('',
    (r'^admin/',include(admin.site.urls)),
    (r'^about/$',direct_to_template,{'template':'about.html'}),  
    (r'^publishers/$',list_detail.object_list,publisher_info),
    (r'^books/$',list_detail.object_list,book_info),
    (r'^books/apress$',list_detail.object_list,apress_books),

)
urlpatterns+=patterns('mysite.books.views',
    (r'^search-form/$','search_form'),
    (r'^search/$','search'),
    #(r'^contact-form/$',views.contact),
    (r'^contact/$','contact'),
    (r'^contact/thanks/$','thanks'),
    (r"^books/([\w'\s]+)$",'books_by_publisher'),
    (r"^authors/(?P<author_id>\d+)/$",'author_detail'),
"""
  return render_to_response("index.html",{"url":url})
"""
def current_datetime(request):
  now=datetime.datetime.now()
  html="<html><body>It is now %s.</body></html>"%now
  return HttpResponse(html)
"""
def current_datetime(request):
  now=datetime.datetime.now()
  return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
  try:
    offset=int(offset)
  except ValueError:
    raise Http404()
  dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
  t=get_Template("hours_ahead.html")
  html=t.render(Context({"offset":offset,"dt":dt}))
#  dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
#  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)

"""
首先，我们从 django.http 模块导入（import） HttpResponse 类。参阅附录 H 了解更多关于 HttpRequest 和 HttpResponse 的细节。 我们需要导入这些类，因为我们会在后面用到。
接下来，我们定义一个叫做hello 的视图函数。
每个视图函数至少要有一个参数，通常被叫作request。 这是一个触发这个视图、包含当前Web请求信息的对象，是类django.http.HttpRequest的一个实例。在这个示例中，我们虽然不用request做任何事情，然而它仍必须是这个视图的第一个参数。
注意视图函数的名称并不重要；并不一定非得以某种特定的方式命名才能让 Django 识别它。 在这里我们把它命名为：hello，是因为这个名称清晰的显示了视图的用意。同样地，你可以用诸如：hello_wonderful_beautiful_world，这样难看的短句来给它命名。 在下一小节（Your First URLconf），将告诉你Django是如何找到这个函数的。
"""

def current_url_view_good(request):
  return HttpResponse("Welcome to the page at %s" %request.path)
"""
def display_meta(request):
  values = request.META.items()
  values.sort()
  html = []
  for k, v in values:
    html.append((k, v,"\n"))
  return render_to_response('request_info.html',{'request_info':html})
#  return HttpResponse('<table>%s</table>' % '\n'.join(html))
"""
def display_meta(request):
  values = request.META.items()
  values.sort()
  html = []
  for k, v in values:
    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#  return render_to_response('request_info.html',{'request_info':'<table>%s</table>' % '\n'.join(html)})
  return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hello1(request):
  return render_to_response('hello.html',{'name':"<script>alert('hello')</script>",'type':'<b>username'})

def about_pages(request,page):
  try:
    return direct_to_template(request,template='about/%s.html'%page)
  except TemplateDoesNotExist:
    raise Http404()

#显示本地图片
import pdb
def my_image(request):
#  pdb.set_trace()
#  image_date=open("/home/jhjguxin/Desktop/djcode/mysite/f_media/img/Firefox_wallpaper.png",'rb').read()
  image_date=open("/home/jhjguxin/Desktop/djcode/mysite/f_media/img/Firefox_wallpaper.png",'rb').read()
  return HttpResponse(image_date,mimetype="image/png")

import csv
#Number of unruly passengers each year 1995-2005.In a real application
#this would likely come from a datebase or some other back-end date store.
UNRULY_PASSENGERS=[146,184,235,200,226,251,299,273,281,304,203]

def unruly_passengers_csv(request):
  #Create the HttpResponse object with the appropriate CSV header.
  response=HttpResponse(mimetype='text/csv')
  response['Content-Disposition']='attachment;filename=unruly.csv'

  #Creat the Csv writer using the HttpResponse as the "file."
  writer=csv.writer(response)
  writer.writerow(['Year','Unruly Airline Passengers'])
  for (year,num)in zip(range(1995,2006),UNRULY_PASSENGERS):
    writer.writerow([year,num])
  return response


