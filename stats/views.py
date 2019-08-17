# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from stats.data_scraper import update_data
from stats.models import StatLine

# Create your views here.
def home(request):
    """
    The first page of the stats app. Not actually called 'home'
        in the url
    """
    #update_data("20182019", False)
    return render(request, 'stats/home.html', {"stat_lines": StatLine.objects.all()})
