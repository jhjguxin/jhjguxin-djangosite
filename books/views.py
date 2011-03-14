#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#views.py
# Create your views here.
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from mysite.books.models import Publisher,Author,Book
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponseRedirect
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
import datetime
def search_form(request):
  return render_to_response('search_form.html')#查找模板文件在templates里面

def search(request):
  errors=[]
  if 'q' in request.GET:# and request.GET['q'](不为空):
    q=request.GET['q']
    if not q:
      errors.append('Enter a search term.')
#     error=True
    elif len(q)>20:
#     error=True
      errors.append('Please enter at most 20 characters')
    else:
      books=Book.objects.filter(title__icontains=q)
      return render_to_response('search_results.html',{'books':books,'query':q})
  return render_to_response('search_form.html',{'errors':errors})
#  else:
#   return HttpResponse('Please submit a search term.')
#   return render_to_response('search_form.html',{'error':True})

"""
def search(request):
    if 'q' in request.GET and request.GET['q']:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
"""

import pdb
from mysite.books.forms import ContactForm
def contact(request):
#  pdb.set_trace()
  if request.method=='POST':
    form=ContactForm(request.POST)
    if form.is_valid():
      ct=form.cleaned_data
      send_mail(
       ct['subject'],
       ct['message'],
       ct.get('email','noreply@example.com'),
       ['siteowner@example.com'],
)
      return HttpResponseRedirect('/contact/thanks/')
  else:
    form=ContactForm(initial={'subject': 'I love your site!'})
  return render_to_response('contact_form.html',{'form':form})

"""
def contact(request):
  errors=[]
  if request.method=='POST':
#    pdb.set_trace()
    if not request.POST.get('subject',''):
      errors.append('Enter a subject.')
    if not request.POST.get('message',''):
      errors.append('Enter a messsage')
    if request.POST.get('email')and'@'not in request.POST['email']:
      errors.append('Enter a valid e-mail address')
    if not errors:
      send_mail(
         request.POST['subject'],
         request.POST['message'],
         request.POST.get('email','noreply@example.com'),
         ['siteowner@example.com'],
)
      return HttpResponseRedirect('/contact/thanks/')
  return render_to_response('contact_form.html',{'errors':errors,
#重定向
    'subject': request.POST.get('subject', ''),
    'message': request.POST.get('message', ''),
    'email': request.POST.get('email', ''),
    })

"""
def thanks(request):
  return HttpResponse("thanks for contact us")
import pdb
def books_by_publisher(request,name):
  #Look up the publisher (and raise a 404 if it can't be found)
  pdb.set_trace()
  publisher=get_object_or_404(Publisher,name__iexact=name)
  #use the object_list view for the heavy lifting.
  return list_detail.object_list(
   request,
   queryset=Book.objects.filter(publisher=publisher),
   template_name='books_by_publisher.html',
   template_object_name='book',
   extra_context={'publisher':publisher}
)

def author_detail(request,author_id):
  #Delegate to the generic view and get an HttpResponse.
  response=list_detail.object_detail(
    request,
    queryset=Author.objects.all(),
    object_id=author_id,
    template_object_name='author',
    template_name='author_detail.html',
)
  #Record the last accessed date.We do this *after* the call
  #to object_detail(),not before it,so that this won't be called
  #unless the Author actually exists.(If the author doesn't exist.)
  #object_detail() will raise Http404,and we won't reach this point.
  now=datetime.datetime.now()
  Author.objects.filter(id=author_id).update(last_accessed=now)
  return response
