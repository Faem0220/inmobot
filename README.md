# inmobot
Sistema para búsqueda y clasificación de inmuebles en alquiler.
## Instalación
- Se necesita tener instalado python
1. Crear directorios y clonar repositorio
`mkdir inmobot`
`cd inmobot`
`git clone < url al repositorio>`
2. Crear y activar entorno virtual
`python3 -m venv env`
`source env/bin/activate`
3. Instalar librerias 
`pip install -r requirements.txt`
4. Crear base de datos
`python3 manage.py makemigrations`
`python3 manage.py migrate`
5. Crear superusuario
`python3 manage.py createsuperuser`
6. Correr servidor local
`cd inmobot`
`python3 manage.py runserver`




