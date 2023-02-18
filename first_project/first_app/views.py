from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord
# Create your views here.

def index(request):
    webpg_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_record': webpg_list}
    return render(request, 'first_app/index.html', context=data_dict)


def index2(request):
    my_dict = {'insert_me': 'heoool from vies.py'}
    return render(request, 'first_app/index2.html', context=my_dict)
