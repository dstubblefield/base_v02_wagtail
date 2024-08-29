# app_forms/mixins.py

from app_snippets.models import County

class OrderedCountyMixin:
    def __init__(self, *args, **kwargs):
        super(OrderedCountyMixin, self).__init__(*args, **kwargs)
        if 'counties' in self.fields:
            self.fields['counties'].queryset = County.objects.order_by('name')
