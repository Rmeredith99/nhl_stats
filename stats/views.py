# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from django.http import HttpResponse

from stats.data_scraper import update_data
from stats.process_filter import filter_text_to_url, update_url, url_string_to_queryset, remove_filter
from stats.process_filter import get_page_number, remove_sort
from stats.process_metric import get_custom_metric
from stats.models import StatLine
from stats.tables import StatLineTable
from stats.filters import StatLineFilter
from stats.forms import FilterForm, MetricForm

# Create your views here.

def home(request):
    """
    The first page of the stats app. Not actually called 'home'
        in the url
    """
    # # If there is a filter submission
    # if request.method == 'POST':
    #     filter_form = FilterForm(request.POST)
    #     if filter_form.is_valid():
    #         # get the filter criteria and the current url
    #         filter_string = filter_form.cleaned_data['filter_string']
    #         current_url = filter_form.cleaned_data['current_url']

    #         # convert the filter criteria into url 
    #         # form and then update current url
    #         filter_url = filter_text_to_url(filter_string)
    #         new_url = update_url("/stats/", current_url, filter_url)
    #         return redirect(new_url)
    #     else:
    #         filter_form = FilterForm()
    # else:
    #     filter_form = FilterForm()

    # update_data("20182019", False)
    objects, filter_box = url_string_to_queryset(request.get_full_path())
    table = StatLineTable(objects)
    page_number = get_page_number(request.get_full_path())
    table.page_number = page_number
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=15)

    return render(request, 'stats/home.html', {"stat_lines": objects, "table": table, "filter_box": filter_box})

def metric_submit(request):
    """
    [metric_submit] is run after entering code into the metric textbox.
        This is only an intermediate step and will eventually redirect
        back to the home page.
        This only runs if the user is logged in.
    """
    # Stopping the action if the user isn't logged in
    if not request.user.is_authenticated:
        # TODO: display a notification here
        print("You need to be logged in to do that")
        return redirect(request.POST['current_url'])

    # If there is a metric submission
    if request.method == 'POST':
        metric_form = MetricForm(request.POST)
        if metric_form.is_valid():
            # get the filter criteria and the current url
            metric_string = metric_form.cleaned_data['metric_string']
            current_url = metric_form.cleaned_data['current_url']
            label = metric_form.cleaned_data['label']
            username = request.user.username

            # metric value stuff
            # TODO:
            # Iterate through CustomStat objects and assign values
            # Change the url with the new id of the CustomMetric
            metric = get_custom_metric(username, label, metric_string)

            return redirect(current_url)
        else:
            metric_form = MetricForm()
            return redirect(request.POST['current_url'])
    else:
        metric_form = MetricForm()
        return redirect("/stats/")


def filter_submit(request):
    """
    [filter_submit] is run after entering a filter into the textbox.
        This is only an intermediate step and will eventually redirect
        back to the home page.
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
            return redirect(request.POST['current_url'])
    else:
        filter_form = FilterForm()
        return redirect("/stats/")

    
def remove_filter_submit(request):
    """
    [remove_filter_submit] takes in a url and removes all parts that
        deal with filters. Returns a new url to redirect to.
    """
    current_url = request.POST.get("current_url")
    new_url = remove_filter(current_url)
    return redirect(new_url)

def remove_sort_submit(request):
    """
    [remove_sort_submit] takes in a url and removes all parts that
        deal with sorting. Returns a new url to redirect to.
    """
    current_url = request.POST.get("current_url")
    new_url = remove_sort(current_url)
    return redirect(new_url)