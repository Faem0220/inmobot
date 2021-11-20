import ast
from datetime import date

date = date.today().isoformat()
print('Ingrese fecha para limpiar')
fecha = input('>')

deptos_dict = open(f"Deptos/dict/Deptos:{fecha}.txt","r")
contents = deptos_dict.read()
dictionary = ast.literal_eval(contents)

selected = open("filter/selected.txt", "r")
sel_cont = selected.read()
selected_list = sel_cont.split(",")

delete = open("filter/delete.txt", "r")
del_cont = delete.read()
delete_list = del_cont.split(",")

lista_nuevos = []
lista_select = []


for i in range(len(dictionary)):
    try:
        print(i)
        if dictionary[i]['Ib'] in delete_list:
            print(dictionary[i]['Ib'],"DELETED")
            del dictionary[i]
            pass
        elif dictionary[i]['Ib'] in selected_list:
            lista_select.append(dictionary[i]);
            print(dictionary[i]['Ib'],"DELETED")
            del dictionary[i]
            pass
        else:
            lista_nuevos.append(dictionary[i]);
    except:
        print("error")
deptos_file = open(f'Deptos/txt/new/new:{date}.txt','w')
for depto in lista_nuevos:
    deptos_file.write(f"Ubicación: {depto['Ubicacion']}"+'\n')
    deptos_file.write(f"Precio Total: ${depto['Precio']}"+'\n')
    deptos_file.write(f"Superficie: {depto['Superficie']}mts2"+'\n')
    deptos_file.write(f"Precio mt2: ${depto['Precio_mt2']}"+'\n')
    deptos_file.write(f"Dormitorios: {depto['Dormitorios']}"+'\n')
    deptos_file.write(f"URL: {depto['URL']}"+'\n')
    deptos_file.write(f"IB: {depto['Ib']}"+'\n')
    deptos_file.write('\n')
    deptos_file.write('------------------------------')
    deptos_file.write('\n')

deptos_select_file = open(f'Deptos/txt/selected/selected:{date}.txt','w')
for depto in lista_select:
    deptos_select_file.write(f"Ubicación: {depto['Ubicacion']}"+'\n')
    deptos_select_file.write(f"Precio Total: ${depto['Precio']}"+'\n')
    deptos_select_file.write(f"Superficie: {depto['Superficie']}mts2"+'\n')
    deptos_select_file.write(f"Precio mt2: ${depto['Precio_mt2']}"+'\n')
    deptos_select_file.write(f"Dormitorios: {depto['Dormitorios']}"+'\n')
    deptos_select_file.write(f"URL: {depto['URL']}"+'\n')
    deptos_select_file.write(f"IB: {depto['Ib']}"+'\n')
    deptos_select_file.write('\n')
    deptos_select_file.write('------------------------------')
    deptos_select_file.write('\n')

