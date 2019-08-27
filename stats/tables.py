import django_tables2 as tables
from stats.models import StatLine
from django.db.models import F
import itertools

class StatLineTable(tables.Table):
    # Adding custom columns to the table
    rank = tables.Column(empty_values=(), orderable=False)
    custom = tables.Column(empty_values=[])

    # Configuring columns so that text doesn't spill over onto a new line
    playerName = tables.Column(attrs={'th': {'style': 'white-space: nowrap'}, 'td': {'style': 'white-space: nowrap'}})
    playerFirstName = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    playerLastName = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    playerBirthCity = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    goals = tables.Column(attrs={'th':{'style': ''}, 'td':{'style': ''}})
    page_number = 1

    def __init__(self, *args, **kwargs):
        super(StatLineTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()
        # default custom_function
        self.custom_function = lambda x : ""

    def render_rank(self):
        return next(self.counter) + 1 + 15 * (self.page_number - 1)

    def render_custom(self, record):
        return record.points - record.ppAssists

    def order_custom(self, QuerySet, is_descending):
        QuerySet = QuerySet.annotate(
            amount = F('points') - F('ppAssists')
        ).order_by(('-' if is_descending else '') + 'amount')
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
