from django import forms

class FilterForm(forms.Form):
    filter_string = forms.CharField(widget = forms.Textarea, initial = "")
    current_url = forms.CharField(max_length = 500, initial = "")

class MetricForm(forms.Form):
    label = forms.CharField(max_length = 200, initial = "")
    metric_string = forms.CharField(widget = forms.Textarea, initial = "")
    current_url = forms.CharField(max_length = 500, initial = "")