from django.shortcuts import render
from django.http import HttpResponse

from kana.models import Kana
from kanji.models import Kanji

# Create your views here.

def index(request):
    num_hiragana = Kana.objects.filter(type__name__iexact='hiragana').count()
    num_katakana = Kana.objects.filter(type__name__iexact='katakana').count()
    num_kanji = Kanji.objects.all().count()
    context={
        'num_hiragana': num_hiragana,
        'num_katakana': num_katakana,
        'num_kanji': num_kanji
    }
    return render(request, 'index.html', context=context)
