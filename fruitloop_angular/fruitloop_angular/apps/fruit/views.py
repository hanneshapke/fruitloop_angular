from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import FruitLocation
from .forms import FruitLocationForm


class FruitLocationCreateView(CreateView):

    model = FruitLocation
    form = FruitLocationForm
    success_url = reverse_lazy('home')
    template = 'fruit/fruitlocation_list.html'
    fields = ['address', 'fruit_type', 'comment']

    def get_context_data(self, **kwargs):
        context = super(FruitLocationCreateView,
                        self).get_context_data(**kwargs)
        context['object_list'] = FruitLocation.objects.all()
        return context
