import django_tables2 as tables
from stats.models import StatLine

class StatLineTable(tables.Table):
    # Configuring columns so that text doesn't spill over onto a new line
    playerName = tables.Column(attrs={'th': {'style': 'white-space: nowrap'}, 'td': {'style': 'white-space: nowrap'}})
    playerFirstName = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    playerLastName = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    playerBirthCity = tables.Column(attrs={'th': {'style': 'white-space: nowrap;'}, 'td': {'style': 'white-space: nowrap;'}})
    goals = tables.Column(attrs={'th':{'style': ''}, 'td':{'style': ''}})

    class Meta:
        model = StatLine
        sequence = ('playerName', 'gamesPlayed', 'goals', 'assists', 'points')
        empty_text = "There are no results for that search"
        exclude = ["id", "playoffs", "year", "playerId"]
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {
            'class': 'table table-sm table-striped table-bordered table-hover table-responsive'
        }
