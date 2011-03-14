#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#view.py
from django.template import Template,Context
from django.template.loader import get_template as get_Template
from django.http import HttpResponse,Http404
import datetime
def hello(request):
  return HttpResponse("Hello world!")

def my_homepage_view(request):
  return HttpResponse("It's jhj's homepage!")
"""
def current_datetime(request):
  now=datetime.datetime.now()
  html="<html><body>It is now %s.</body></html>"%now
  return HttpResponse(html)
"""
def current_datetime(request):
  now=datetime.datetime.now()
  t=get_Template("current_datetime.html")#实际内建函数名是get_template
  html=t.render(Context({'current_date':now}))
  return HttpResponse(html)

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
