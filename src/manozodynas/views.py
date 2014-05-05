from django.shortcuts import render
from .models import KlaseWord
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def words_view(request):
    return render(request, 'manozodynas/words_view.html', {'zodziai': KlaseWord.objects.all()})

class NewWord(CreateView):
    model = KlaseWord
    success_url = reverse_lazy('words_view')
    template_name = 'manozodynas/enter_word.html'
