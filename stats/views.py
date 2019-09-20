# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.parse import urlencode, quote

from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from django.http import HttpResponse

from stats.data_scraper import update_data
from stats.process_filter import filter_text_to_url, url_string_to_queryset
from stats.process_metric import get_custom_metric, assign_values

from stats.models import StatLine, CustomMetric
from stats.tables import StatLineTable
from stats.filters import StatLineFilter
from stats.forms import FilterForm, MetricForm

# Create your views here.

def params_GET_to_url(params):
    """
    [params_GET_to_url] takes in GET parameters and creates a url
        from those.
    params: Dict
    """
    # If there are not GET parameters, return empty string
    if params == {}:
        return ""
    url = ["?"]
    for key in ["filter", "metric", "sort", "page"]:
        if key in params:
            url.append(key + "=" + params[key][0] + "&")
    url_string = "".join(url).strip("&")

    return url_string.replace(",", "%2C").replace("~", "%7E")


def home(request):
    """
    The first page of the stats app. Not actually called 'home'
        in the url. Displays the main content of the website, the 
        table of data and metric submission system.
    """
    params_GET = dict(request.GET)

    # Defining the part of the URL that corresponds to filtering
    # and using that to create a set of filtered objects
    filter_string = params_GET.get("filter", [""])[0].replace(",", "%2C").replace("~", "%7E")
    objects, filter_box = url_string_to_queryset(filter_string)

    # Insertion of custom metric:
    # - retrieve metric number
    # - apply metric to objects to create CustomStat objects
    metric_id = -1
    metric_string = ""
    metric_message = ""
    if 'metric' in params_GET:
        try:
            metric_id = int(params_GET['metric'][0])
            metric = CustomMetric.objects.get(pk=metric_id)
            metric_message = assign_values(metric, objects)
            metric_string = metric.string
        except:
            metric_message = ""
            metric_id = -1
        
    table = StatLineTable(objects)

    table.metric_id = metric_id

    # Setting page number for the table so the correct ranks are displayed
    page_number = int(params_GET.get("page", ["1"])[0])
    table.page_number = page_number

    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=15)

    return render(request, 'stats/home.html', {
        "stat_lines": objects, 
        "table": table, 
        "filter_box": filter_box, 
        "metric_box": metric_string,
        "metric_message": metric_message,
        })


def metric_submit(request, s = ""):
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
            username = request.user.username

            # metric value stuff
            metric = get_custom_metric(username, "default", metric_string)
            metric_id = metric.id

            # getting the GET params and changing them to reflect the metric
            params_GET = dict(request.GET)
            params_GET["metric"] = [str(metric_id)]

            # Encode the GET parameters as url
            new_url = "/stats/" + params_GET_to_url(params_GET)
            return redirect(new_url)
        else:
            metric_form = MetricForm()
            return redirect(request.POST['current_url'])
    else:
        metric_form = MetricForm()
        return redirect("/stats/")


def filter_submit(request, s=""):
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
            # form and then update the GET parameters
            filter_url = filter_text_to_url(filter_string)
            params_GET = dict(request.GET)
            # A new filter can cause the page number to be over max pages
            # To fix this, reset page for every new filter
            if "page" in params_GET:
                del(params_GET["page"])

            # We only want to update the filter part of the url if there isn't an error
            if filter_url != "":
                params_GET["filter"] = [filter_url]

            # Encode the GET parameters as url
            new_url = "/stats/" + params_GET_to_url(params_GET)
            return redirect(new_url)
        else:
            filter_form = FilterForm()
            return redirect(request.POST['current_url'])
    else:
        filter_form = FilterForm()
        return redirect("/stats/")

    
def remove_filter_submit(request, s=""):
    """
    [remove_filter_submit] takes in a url and removes all parts that
        deal with filters. Returns a new url to redirect to. Additionally
        removes the page number since that will become irrelevant due to
        a new set of objects.
    """
    params_GET = dict(request.GET)
    if "filter" in params_GET:
        del(params_GET["filter"])
    if "page" in params_GET:
        del(params_GET["page"])
    new_url = "/stats/" + params_GET_to_url(params_GET)

    return redirect(new_url)

def remove_sort_submit(request, s=""):
    """
    [remove_sort_submit] takes in a url and removes all parts that
        deal with sorting. Returns a new url to redirect to. Additionally
        removes the page number since that will become irrelevant due to
        a new ordering of objects.
    """
    params_GET = dict(request.GET)
    if "sort" in params_GET:
        del(params_GET["sort"])
    if "page" in params_GET:
        del(params_GET["page"])
    new_url = "/stats/" + params_GET_to_url(params_GET)

    return redirect(new_url)