import django_tables2 as tables
from stats.models import StatLine, CustomMetric, CustomStat
from django.db.models import F, Max
import itertools

template = '''
{% for item in record.customstat_set.all %}
    {{ item.value }}
{% endfor %}
'''

class StatLineTable(tables.Table):
    # Adding custom columns to the table
    rank = tables.Column(empty_values=(), orderable=False)
    custom = tables.Column(empty_values = (), accessor = "custom_stat_player", verbose_name = "Custom")

    # Configuring columns so that text doesn't spill over onto a new line
    playerName = tables.Column(attrs={'th': {'style': 'white-space: nowrap'}, 'td': {'style': 'white-space: nowrap'}})
    playerFirstName = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    playerLastName = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    playerBirthCity = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})

    page_number = 1
    metric_id = -1

    def __init__(self, *args, **kwargs):
        super(StatLineTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()
        # default custom_function
        self.custom_function = lambda x : ""

    def render_rank(self):
        """
        [render_rank] is responsible for returning the correct rank number
            next to the player name. Associated with the 'rank' column
            through django-tables2 code.
        """
        return next(self.counter) + 1 + 15 * (self.page_number - 1)

    def render_custom(self, value):
        """
        [render_custom] is responsible for returning the custom metric
            value for each player. Associated with the 'custom' column
            through django-tables2 code.
        """
        try:
            stat = value.get(metric__id = self.metric_id)
            return stat.value
        except:
            return ""

    def order_custom(self, QuerySet, is_descending):
        """
        [order_custom] over-rides the default ordering for custom values
            displayed in the table. Associated with the 'custom' column
            through django-tables2 code.
        """
        QuerySet = QuerySet.filter(
            custom_stat_player__metric__id = self.metric_id 
        ).order_by(
            ('-' if is_descending else '') + 'custom_stat_player__value'
        )
        return (QuerySet, True)

    class Meta:
        model = StatLine
        sequence = ('rank', 'playerName', 'custom', 'gamesPlayed', 'goals', 'assists', 'points')
        empty_text = "There are no results for that search"
        exclude = ["id", "playoffs", "year", "playerId"]
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {
            'class': 'table table-sm table-striped table-bordered table-hover table-responsive'
        }
