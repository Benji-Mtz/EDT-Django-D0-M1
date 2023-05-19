# Primeros pasos en Django

## Configurando una nueva base de datos, segun nuestro docker

```sh
# setting.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "edteam_db",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```
```yml

version: '2'
services:
  postgres:
    image: 'postgres:latest'
    restart: always
    volumes:
      - './postgres_data:/var/lib/postgresql/data'
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=edteam_db
    ports:
      - '5432:5432'

```
Ir al modelo o clase de donde se creo la tabla de la db y pasar ``managed=False`` a True

```py
    class Meta:
        managed = True
```

Corremos el archivo ``docker-compose.yaml`` con `docker-compose.yml up -d`

Si ya teniamos las migraciones con sqlite, requerimos rehacer estas para postgresql

```sh
λ python manage.py makemigrations
λ python manage.py migrate
λ python manage.py createsuperuser # admin:admin
λ python manage.py runserver
```
Ahora podemos ir a `http://127.0.0.1:8000/admin/` y hacer el crud de la data

