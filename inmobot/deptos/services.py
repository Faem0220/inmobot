from .models import Inmueble
from .scrap.scrap import buscar_deptos


def extract_data_deptos():
    lista_deptos = buscar_deptos(50000)
    for depto in lista_deptos:
        try:
            depto = Inmueble.objects.create(
                location = depto['Ubicacion'],
                price = depto['Precio'],
                area = depto['Superficie'],
                mt_price = depto['Precio_mt2'],
                rooms = depto['Dormitorios'],
                pub_date = depto['Publicacion'],
                ib = depto['Ib'],
                url = depto['URL']
            )
            depto.save()
        except Exception as e:
            print(e)
    return lista_deptos

def clean_list(selected,deleted):
    for sel in selected:
        depto_sel = Inmueble.objects.get(ib=sel)
        depto_sel.status = 'SEL'
        depto_sel.save()
    for delete in deleted:
        depto_del = Inmueble.objects.get(ib=delete)
        depto_del.status = 'DEL'
        depto_del.save()
    return ""
