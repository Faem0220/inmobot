from django.shortcuts import render
from .models import Inmueble
from .services import clean_list,extract_data_deptos

# Create your views here.
selected = []
deleted = []
def deptos_list(request):
    new = Inmueble.objects.filter(status='NEW').order_by('mt_price')
    if request.method == "POST":
        if 'select' in request.POST:
            selected = request.POST.getlist('selected')
            deleted = request.POST.getlist('deleted')
            print(selected)
            print(deleted)
            clean_list(selected,deleted)
        elif 'scrap' in request.POST:
            extract_data_deptos()
            print('SCRAP')
    return render(request, 'deptos/deptos_list.html', {'deptos': new})

def selected_list(request):
    sel = Inmueble.objects.filter(status='SEL').order_by('mt_price')
    return render(request, 'deptos/deptos_list.html', {'deptos': sel})