from django.shortcuts import redirect, render
from .models import Inmueble
from .services import clean_list,extract_data_deptos

# Create your views here.
selected = []
deleted = []
def deptos_list(request):
    all = Inmueble.objects.all()
    return render(request, 'deptos/deptos_list.html', {'deptos': all})
def new_deptos_list(request):
    # GET
    new = Inmueble.objects.filter(user=request.user,status='NEW').order_by('mt_price')

    #POST
    #receive list of objects from form and call clean_list
    if request.method == "POST":
        if 'select' in request.POST:
            selected = request.POST.getlist('selected')
            deleted = request.POST.getlist('deleted')
            print(selected)
            print(deleted)
            clean_list(selected,deleted)
        elif 'scrap' in request.POST:
            #extract_data_deptos(request.user)
            print('SCRAP')
    return render(request, 'deptos/new_deptos_list.html', {'deptos': new})


def search_deptos(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            precio_max = request.POST.get('precio_max')
            ciudad = request.POST.get('ciudad')
            dormitorios = request.POST.get('dormitorios')
            extract_data_deptos(request.user,ciudad,precio_max,dormitorios)
            redirect('deptos/deptos_list.html')
    return render(request, 'deptos/search_deptos.html')
def selected_list(request):
    sel = Inmueble.objects.filter(status='SEL').order_by('mt_price')
    return render(request, 'deptos/deptos_list.html', {'deptos': sel})