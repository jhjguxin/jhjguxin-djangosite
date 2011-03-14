#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#admin.py

from django.contrib import admin
from mysite.books.models import Publisher,Author,Book


class AuthorAdmin(admin.ModelAdmin):
  list_display=('first_name','last_name','email','last_accessed')
  search_fields=('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
  list_display=('title','publisher','publication_date')#不能简单的加入'authors' 一对多类型
  list_filter=('publication_date',)
  date_hierarchy='publication_date'
  ordering=('-publication_date',)
#  fields=('title',)#请注意移除fields选项，以使得编辑页面包含所有字段。）
  filter_horizontal = ('authors',)
#  filter_vertical=('authors',)
#  raw_id_fields=('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)




