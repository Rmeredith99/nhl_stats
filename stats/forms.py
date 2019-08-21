from django import forms

class FilterForm(forms.Form):
    filter_string = forms.CharField(widget = forms.Textarea, initial = "")
    current_url = forms.CharField(max_length = 300, initial = "")

class MetricForm(forms.Form):
    metric_string = forms.CharField(widget = forms.Textarea, initial = "")
    current_url = forms.CharField(max_length = 300, initial = "")