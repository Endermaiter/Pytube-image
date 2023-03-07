![img1](https://raw.githubusercontent.com/docker-library/docs/c350af05d3fac7b5c3f6327ac82fe4d990d8729c/docker/logo.png)

# PROCESO EXPLICADO PASO A PASO

Imagen de Docker Hub --> [Imagen](https://hub.docker.com/repository/docker/endermaiter/datatube/general)
-------------------------------

## 1. Crear proyecto de PyCharm

   Creamos un proyecto de Pycharm con un subdirectorio llamado *app*, donde estara el script de python.

## 2. Crear y codificar un script de python

   Creamos un script nuevo de python (o modificamos el que crea el IDE por defecto) y lo llamamos por ejemplo *miscript.py*. Dentro codificaremos un pequeño script que nos dará los datos del video de YouTube que nosotros elijamos. En mi caso, quedó algo así:

```
url = input("Introduce la url de un video:")

video = YouTube(url)

# Titulo
print("Titulo: ", video.title)
# Visualizaciones
print("Views: ", video.views)
# Duracion
print("Duracion: ", video.length, " segundos")
# Descripcion
print("Descripcion: " + video.description)
# Data
print("Rating: ", video.rating)

if __name__ == '__main__':
    print("Execute Successful")
```

## 3. Crear y configurar un Dockerfile

Creamos un nuevo archivo llamado *Dockerfile* en el que pondremos jugar con la personalización de nuestra imagen. En mi caso, quedó asi:

```
FROM python:3

WORKDIR /usr/src/app

RUN pip install pytube

COPY ./app /usr/src/app

CMD ["python", "miscript.py"]
```
Explicación del Dockerfile: (WIP)

* ``FROM python:3``: La base de nuestra imagen

* ``WORKDIR /usr/src/app``: directorio donde estarán los archivos del contenedor

* ``RUN pip install pytube``: Instruccion que se ejecuta al momento de crear la imagen

* ``COPY ./app /usr/src/app``: Copia todos los archivos que se encuentran en ./app ---> /usr/src/app

* ``CMD ["python", "miscript.py"]``: Comando en el proceso de inicio del contenedor


## 4. Crear la imagen personalizada

  Una vez creado el *Dockerfile*, solo nos quedara hacer la build de nuestra imagen. Para ello, ejecutaremos el siguiente comando:

   ``$docker build -t  marcosimage-pytube:latest .``

Explicación del comando:

* ``$docker build``: Comando docker (palabras reservadas)

* ``-t``: o --tag, indica que usará un tag

* ``marcosimage-pytube``: Nombre de la imagen

* ``:latest``: Tag de nuestra imagen que usaremos para identificarla mas adelante.

Ahora podremos hacer un run con nuestra imagen ya creada usando el siguiente comando:

$docker run -i marcosimage-pytube:latest

``-i``: Este parámetro lo he usado para crear un contenedor interactivo ya que en el script de Python  he puesto un input() para poder introducir el video que el usuario quiera.

## 5. Crear cuenta de Docker Hub

Para conseguir el objetivo de que cualquier persona pueda descargar nuestra imagen, lo primero que tendremos que hacer será subirlo a la nube. Por lo tanto nos creamos una cuenta en [Docker](https://hub.docker.com/).

## 6. Crear repositorio en Docker Hub

Cuando tengamos la cuenta creada y estemos logeados, creamos un nuevo repositorio dentro de ella. El nombre que le pongamos a este repositorio es muy importante porque será necesario utilizarlo mas tarde.

## 7. Relacionar la imagen con el repositorio

Ahora que tenemos tanto la imagen como el repositorio en la nube creados, procedemos a vincular ambas partes con el siguiente comando:

``$docker tag marcosimage-pytube:latest endermaiter/datatube:latest``

Explicación del comando:

* ``$docker tag``: Instrucción docker

* ``marcosimage-pytube:latest``: nombreimagen:tagimagen (deben ser los usados en el comando del build anteriormente ejecutado)

* ``endermaiter/datatube:latest``: nombreusuaro/nombrerepositorio:tag (el nombre de usuario debe ser el usado al crear la cuenta de Docker Hub, el nombre del repostorio debe ser el que hemos escrito al crearlo y el tag debe ser el que hemos usado en el build o en el parámetro anterior)

## 8. Subir la imagen al repositorio

Ahora que estan vinculadas, nos logeamos con nuestra cuenta de Docker Hub en la terminal con el siguiente comando:

``$docker login``

Y por ultimo, subimos la imagen al repositorio con el siguiente comando:

``$docker push endermaiter/datatube:latest``

Explicación del comando:

* ``$docker push``: Instrucción de Docker

* ``endermaiter/datatube:latest``: nombreUsuario/nombrerepositorio:tag
