from django.views import generic
from .models import Wikis

# Create your views here.

class WikisList(generic.ListView):
    queryset = Wikis.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 3

class WikisDetail(generic.DetailView):
    model = Wikis
    template_name = 'wiki_detail.html'
