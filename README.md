# SanjuanEnriquezBrandonAlexisUnidad2

## FinanTrack — Sistema de Control de Gastos

Proyecto desarrollado para la materia **Desarrollo Web Integral**, correspondiente a la Unidad 2.

FinanTrack es una aplicación web desarrollada con Django que permite llevar un control básico de los movimientos financieros de un usuario, registrando ingresos y gastos, clasificándolos por categorías y mostrando un resumen del estado financiero.

## Tecnologías utilizadas

* Python 3.14.6
* Django 6.1.1
* SQLite
* HTML5
* CSS3
* Git
* GitHub
* Visual Studio Code

## Funcionalidades

* Inicio de sesión de usuarios.
* Registro de movimientos financieros.
* Clasificación de movimientos como ingresos o gastos.
* Categorías para organizar los movimientos.
* Cálculo de ingresos, gastos y saldo disponible.
* Visualización de movimientos registrados.
* Eliminación de movimientos.
* Panel principal para consultar el resumen financiero.
* Protección de las funciones principales mediante autenticación.

## Estructura del proyecto

```text
SanjuanEnriquezBrandonAlexisUnidad2/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── finanzas/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── .gitignore
└── README.md
```

## Control de versiones

El proyecto utiliza **Git** para controlar los cambios realizados durante el desarrollo y **GitHub** como repositorio remoto.

El flujo utilizado consiste en:

1. Realizar cambios en el proyecto.
2. Verificar el funcionamiento de la aplicación.
3. Revisar los archivos modificados mediante `git status`.
4. Preparar los cambios con `git add`.
5. Crear un commit descriptivo con `git commit`.
6. Enviar los cambios al repositorio remoto mediante `git push`.

## Instalación y ejecución

Para ejecutar el proyecto de manera local es necesario contar con Python instalado.

Crear y activar el entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Instalar Django:

```bash
python -m pip install django
```

Ejecutar las migraciones:

```bash
python manage.py migrate
```

Iniciar el servidor:

```bash
python manage.py runserver
```

Después se puede acceder a la aplicación desde:

```text
http://127.0.0.1:8000/
```

## Repositorio

Repositorio oficial del proyecto:

https://github.com/BrandonSanjuan/SanjuanEnriquezBrandonAlexisUnidad2
