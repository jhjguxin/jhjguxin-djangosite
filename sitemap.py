#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#sitemap.py
from django.contrib.sitemaps import Sitemap
from mysite.books.models import Book

class BookSitemap(Sitemap):
  changefreq = "never"
  priority = 0.5


  def items(self):
    return Book.objects.filter(is_draft=False)

  def lastmod(self, obj):
    return obj.publication_date

