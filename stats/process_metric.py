from stats.models import StatLine, CustomStat, CustomMetric
from django.db.models import Avg
from django.db import transaction
from time import time


def statline_to_value(statline_object, total_objects, custom_string):
    """
    [statline_to_value] is called from views when a metric is submitted.
    [statline_object]: instance of StatLine
    [custom_string]: string
    Returns: float
    """
    # TODO: write code to process custom_string and output a related
    # value instead of a hard-coded one
    return total_objects.aggregate(Avg('goals'))['goals__avg']

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
        for stat in metric.customstat_set.all():
            stat.delete()
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
    time_a = time()
    delete_metric_stats(metric)
    metric_string = metric.string

    stats = [
        CustomStat(
            player = statline, 
            value = statline_to_value(statline, objects, metric_string), 
            metric = metric
            ) for statline in objects
        ]
    CustomStat.objects.bulk_create(stats)
    time_b = time()
    print(time_b - time_a)

    # for statline in objects:
    #     value = statline_to_value(statline, objects, metric_string)
    #     stat = CustomStat(player = statline, value = value, metric = metric)
    #     stat.save()
    # time_b = time()
    # print(time_b - time_a)


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