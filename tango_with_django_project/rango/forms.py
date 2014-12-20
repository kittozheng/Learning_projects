#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from rango.models import UserProfile, Page, Category

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

class CategoryForm(forms.ModelForm):
    name_regex = [RegexValidator(ur'^[a-zA-Z0-9\u4e00-\u9fa5]*$',
                                 message="Alpha, chinese and number are supported!")]

    name = forms.CharField(validators=name_regex,max_length=128, help_text="Please enter the categpry name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fileds = ('name',)

class PageForm(forms.ModelForm):
    title_regex = [RegexValidator(ur'^[a-zA-Z0-9\u4e00-\u9fa5]*$',
                                 message="Alpha, chinese and number are supported!")]

    title = forms.CharField(validators=title_regex, max_length=128, help_text="Please enter the title")
    url = forms.URLField(max_length=200, help_text="Please enter the URL")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            cleaned_data['url'] =  'http://' + url
        
        return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)
