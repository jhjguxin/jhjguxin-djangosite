#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#forms.py

from django import forms

class ContactForm(forms.Form):
  subject=forms.CharField(max_length=100)
  email=forms.EmailField(required=False,label='You e-mail address')
  message=forms.CharField(widget=forms.Textarea,min_length=5)
