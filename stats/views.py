# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from stats.data_scraper import update_data
from stats.process_filter import filter_text_to_url, update_url, url_string_to_queryset
from stats.models import StatLine
from stats.tables import StatLineTable
from stats.filters import StatLineFilter
from stats.forms import FilterForm

# Create your views here.

def home(request):
    """
    The first page of the stats app. Not actually called 'home'
        in the url
    """
    # If there is a filter submission
    if request.method == 'POST':
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            # get the filter criteria and the current url
            filter_string = filter_form.cleaned_data['filter_string']
            current_url = filter_form.cleaned_data['current_url']

            # convert the filter criteria into url 
            # form and then update current url
            filter_url = filter_text_to_url(filter_string)
            new_url = update_url("/stats/", current_url, filter_url)
            return redirect(new_url)
        else:
            filter_form = FilterForm()
    else:
        filter_form = FilterForm()

    # update_data("20182019", False)
    # objects = StatLine.objects.all()
    objects = url_string_to_queryset(request.get_full_path())
    #objects = objects.filter(points__lt = 100)
    table = StatLineTable(objects)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=15)

    return render(request, 'stats/home.html', {"stat_lines": objects, "table": table})
