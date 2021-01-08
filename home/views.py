from django.shortcuts import render
from django.http import HttpResponse

from kana.models import Kana

# Create your views here.

def index(request):
    num_hiragana = 0#Kana.objects.filter(type__name__iexact='hiragana').count()
    num_katakana = 0#Kana.objects.filter(type__name__iexact='katakana').count()
    context={
        'num_hiragana': num_hiragana,
        'num_katakana': num_katakana
    }
    return render(request, 'index.html', context=context)
