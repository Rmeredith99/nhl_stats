# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    """
    The first page of the stats app. Not actually called 'home'
        in the url
    """
    return render(request, 'stats/home.html', {})
