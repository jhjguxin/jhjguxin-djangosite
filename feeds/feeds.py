#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#feeds.py
from django.contrib.syndication.feeds import Feed
from mysite.books.models import Book,Author
class LatesEntries(Feed):
  title="书名"
  authors="作者"
  publisher='出版社'
  publication_date='出版日期'
  link="http://127.0.0.1:8000/books/archive/"
  description="The latest news about stuff."
  item_link='/books/'
  def items(self):
    return Book.objects.order_by('-publication_date')[:5]
#  def items(self):
#    return Author.objects.order_by('-last_accessed')[:5]


