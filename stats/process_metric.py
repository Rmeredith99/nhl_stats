from stats.models import StatLine, CustomStat, CustomMetric
from stats.interpreter import interpreter
from django.db.models import Avg
from django.db import transaction
from time import time


def get_custom_metric(username, label, metric_string):
    """
    [get_custom_metric] returns a CustomMetric object with fields
        equal to username and metric_string. If there is currently
        a metric with the same values, it will delete it and create
        a new one to return.
    [username]: string
    [label]: string
    [metric_string]: string
    Returns: CustomMetric object
    """
    metric_queryset = CustomMetric.objects.filter(
        username__exact = username
    ).filter(
        label__exact = label
    )

    if len(metric_queryset) > 0:
        metric = metric_queryset.get(username = username)
        metric.customstat_set.all().delete()
        # for stat in metric.customstat_set.all():
        #     stat.delete()
        metric.delete()

    # If there is no current metric with the given values
    metric = CustomMetric(username = username, label = label, string = metric_string)
    metric.save()

    return metric

@transaction.atomic
def assign_values(metric, objects):
    """
    [assign_values] takes in a metric object and a queryset of StatLine
        objects and creates a CustomStat for each statline in the queryset.
    [metric]: CustomMetric object
    [objects]: StatLine queryset
    Returns: None
    """
    delete_metric_stats(metric)
    metric_string = metric.string

    # statline_to_value is a function that optimizes for repeated
    # calculation of aggregate functions
    # Takes in a statline and returns a float or error
    statline_to_value = interpreter(metric_string, objects)

    stats = [
        CustomStat(
            player = statline, 
            value = statline_to_value(statline), 
            metric = metric
            ) for statline in objects
        ]
    CustomStat.objects.bulk_create(stats)

def add_metric(url, metric_id):
    """
    [add_metric] takes in a url and an id indicating the metric and 
        returns a new url with the id within it.
    [url]: string
    [metric_id]: int
    """
    if "?" in url:
        return url + "&metric=" + str(metric_id)
    else:
        return url + "?metric=" + str(metric_id)

def delete_metric_stats(metric):
    """
    [delete_metric_stats] is used to delete all CustomStat objects associate
        with the given metric. This is to be called right before assigning 
        new objects to the metric so that all old objects are cleared.
    [metric]: CustomMetric object
    """
    for stat in metric.customstat_set.all():
        stat.delete()