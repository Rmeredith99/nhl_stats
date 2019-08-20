from stats.tables import StatLineTable
from stats.models import StatLine 
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class StatLineFilter(SingleTableMixin, FilterView):
    table_class = StatLineTable
    model = StatLine
    template_name = 'django_tables2/bootstrap4.html'