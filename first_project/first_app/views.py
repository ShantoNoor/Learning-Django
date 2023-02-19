from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage
from . import forms

# Create your views here.

def index(request):
    webpg_list = AccessRecord.objects.order_by('date')
    webpgs = Webpage.objects.all()

    data_dict = {'access_record': webpg_list, 'webpgs': webpgs}

    return render(request, 'first_app/index.html', context=data_dict)


def index2(request):
    my_dict = {'insert_me': 'heoool from vies.py'}
    return render(request, 'first_app/index2.html', context=my_dict)


def form_input(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            print(f'Name: {name}')
            print(f'Email: {email}')
            print(f'Text: {text}')

    return render(request, 'first_app/form.html', {'form': form})


def web_form(request):
    form = forms.WebFrom()

    if request.method == 'POST':
        form = forms.WebFrom(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("From is not valid")

    return render(request, 'first_app/web_form.html', {'form': form})

