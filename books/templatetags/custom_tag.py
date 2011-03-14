#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django import template

register = template.Library()

@register.tag(name='current_time')
def do_current_time(parser, token):
#  pdb.set_trace()  
  try:
    # split_contents() knows not to split quoted strings.
    tag_name, format_string = token.split_contents()
  except ValueError:
    msg = '%r tag requires a single argument' % token.split_contents()[0]
    raise template.TemplateSyntaxError(msg)
  return CurrentTimeNode(format_string[1:-1])

import datetime

class CurrentTimeNode(template.Node):
  def __init__(self, format_string):
    self.format_string = str(format_string)
  
  def render(self, context):
#    pdb.set_trace()
    now = datetime.datetime.now()
    return now.strftime(self.format_string)
#register.tag('current_time', do_current_time)#实例化

