from bs4 import BeautifulSoup
import requests
from datetime import date
import time


date = date.today().isoformat()

def buscar_deptos(precio_max):
    # Extrae de la url departamentos segun filtros y los almacena en la base de datos
    lista_deptos = []

    pages = 10
    for page in range(1,pages):
        url = f'https://www.inmobusqueda.com.ar/departamento-la-plata-casco-urbano-0-{precio_max}-pesos-pagina-{page}.html?cdormitorios=1.'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        # Se selecciona el cuadro con los datos de las casas para extraer datos
        datos = soup.find_all('div', class_= 'resultadoContenedorDatosResultados')
        # Se extrae cantidad de páginas
        pages = soup.find_all('div',class_="paginas")[1].text[-2:]
        # Se recorren todos los cuadros de datos
        for dato in datos:
            try:
                ubicacion = dato.find('a').text
                precio = dato.find('div', class_= 'resultadoPrecio').text
                # Se omiten las que no tienen precio
                if precio.startswith('Consulte'):
                    continue
                else:
                    t_precio = ((precio.replace('$','').replace('.','')))
                    # Se filtran las que tienen expensas en el precio y se suma al precio
                    if 'Expensas' in t_precio:
                        con_expensas = t_precio.split('Expensas :')
                        t_precio = int(con_expensas[0]) + int(con_expensas[1])
                    t_precio = int(t_precio)
                    lista_info = dato.find('div', class_= 'resultadopublica').text.split()
                    dormitorios = lista_info[0]
                    fecha_pub = lista_info[-1]
                    ib = lista_info[-2]
                    link = dato.find('a')['href']
                    try:
                        mts2 = float(lista_info[2])
                    except:
                        print('Superficie con mal formato')
                    # Se agregan a la lista solo las que tienen precio distinto de 0
                    if mts2 > 0:
                        precio_mt2 = t_precio / mts2
                        Depto = dict(Ubicacion=ubicacion,
                                    Precio=t_precio,
                                    Superficie=mts2,
                                    Precio_mt2=round(precio_mt2),
                                    Dormitorios=dormitorios,
                                    Publicacion=fecha_pub,
                                    Ib=ib,
                                    URL=link)
                        lista_deptos.append(Depto)
            except:
                print('error en formato')
        time.sleep(5)
 
    lista__ordenada = sorted(lista_deptos, key=lambda k: k['Precio_mt2'])
    # se retorna la lista de dict
    return lista__ordenada
