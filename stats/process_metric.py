from stats.models import StatLine, CustomStat, CustomMetric

def statline_to_value(statline_object, custom_string):
    """
    [statline_to_value] is called from views when a metric is submitted.
    [statline_object]: instance of StatLine
    [custom_string]: string
    """
    # TODO: write code to process custom_string and output a related
    # value instead of a hard-coded one
    return statline_object.points - statline_object.assists1st

def get_custom_metric(username, label, metric_string):
    """
    [get_custom_metric] returns a CustomMetric object with fields
        equal to username and label if one exists. Otherwise, 
        returns a new object with instantiated CustomStat objects
        associated with it. 
        NOTE: This does not set the value for the stat objects.
    [username]: string
    [label]: string
    [metric_string]: string
    """
    metric_queryset = CustomMetric.object.filter(
        username__exact = username
    ).filter(
        label__exact = label
    )

    if len(metric_queryset) > 0:
        metric = metric_queryset.get(username = username)
        metric.string = metric_string
        metric.save()

    else: # If there is no current metric with the given values
        metric = CustomMetric(username = username, label = label, string = metric_string)
        metric.save()
        # Creating a CustomStat object for every statline
        for player in StatLine.objects.all():
            stat = CustomStat(player = player, metric = metric)
            stat.save()

    return metric

