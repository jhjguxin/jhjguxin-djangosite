#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models
import datetime
"""
我们来假定下面的这些概念、字段和关系：

    * 一个作者有姓，有名及email 地址。

    * 出版商有名称，地址，所在城市、省，国家，网站。

    * 书籍有书名和出版日期。 它有一个或多个作者（和作者是多对多的关联关系[many-to-many]）， 只有一个出版商（和出版商是一对多的关联关系[one-to-many]，也被称作外键[foreign key]）
"""
# Create your models here.
#出版商有名称，地址，所在城市、省，国家，网站。
class Publisher(models.Model):
  name=models.CharField(max_length=30)
  address = models.CharField(max_length=50)
  city=models.CharField(max_length=60)
  state_province=models.CharField(max_length=30)
  country=models.CharField(max_length=50)
  website=models.URLField()
  def __unicode__(self):
    return self.name
  class Meta(object):
    ordering=['name']
#一个作者有姓，有名及email 地址。
class Author(models.Model):
  first_name=models.CharField(max_length=30)
  last_name=models.CharField(max_length=40)
  email=models.EmailField(blank=True,verbose_name='e-mail')
  last_accessed=models.DateField(default=datetime.datetime.now())
  def __unicode__(self):
      return u'%s %s'%(self.first_name,self.last_name)
#书籍有书名和出版日期。 它有一个或多个作者（和作者是多对多的关联关系[many-to-many]）， 只有一个出版商（和出版商是一对多的关联关系[one-to-many]，也被称作外键[foreign key]）
import pdb
class BookManager(models.Manager):
#  pdb.set_track()
  def title_count(self,keyword):
    return self.filter(title_icontains=keyword).count()

"""
修改初始Manager QuerySets

一个manager的基本QuerySet返回系统中的所有objects. 例如,Book.objects.all返回数据库book中的所有书本.

我们可以通过覆盖Manager.get_query_set()方法来覆盖manager的基本 QuerySet. get_query_set()按照你的要求返回一个QuerySet.
"""

#First,define the Manger subclass.
class DahlBookManager(models.Manager):
  def get_quer_set(self):
    return super(DahlBookManager,self).get_quer_set().filter(author='Roald Dahl')
#Then book it into the Book model explicitly.
#dahl_objects = DahlBookManager() # The Dahl-specific manager.


class Book(models.Model):
  title=models.CharField(max_length=100)
  authors=models.ManyToManyField(Author)
  publisher=models.ForeignKey(Publisher)
  publication_date=models.DateField(blank=True,null=True)
  objects=BookManager()
  dahl_objects = DahlBookManager() # The Dahl-specific manager.
  def __unicode__(self):
    return self.title

