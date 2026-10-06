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
* Render

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

## Acceso al sistema publicado

El proyecto se encuentra disponible en la siguiente dirección:

**https://finantrack-od4d.onrender.com/**

### Cuenta de demostración

Para revisar las funciones principales del sistema se puede utilizar la siguiente cuenta:

* **Usuario:** `admin`
* **Contraseña:** `FinanTrack2026`

Estas credenciales corresponden a una cuenta creada exclusivamente para la demostración del proyecto académico.

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
├── build.sh
├── requirements.txt
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

Durante el desarrollo se realizaron diferentes commits para registrar el avance del proyecto y mantener un historial de cambios.

## Despliegue en la nube

Para publicar la aplicación se utilizó **Render**, conectado directamente con el repositorio de GitHub.

El proceso de despliegue utiliza:

* Python 3.
* Archivo `requirements.txt` para instalar las dependencias.
* Archivo `build.sh` para ejecutar la instalación, generación de archivos estáticos y migraciones.
* Gunicorn como servidor para ejecutar la aplicación Django.
* Variables de entorno para configurar la aplicación en producción.

La aplicación publicada puede consultarse en:

**https://finantrack-od4d.onrender.com/**

## Instalación y ejecución local

Para ejecutar el proyecto de manera local es necesario contar con Python instalado.

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

En Git Bash:

```bash
source .venv/Scripts/activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar las migraciones

```bash
python manage.py migrate
```

### Iniciar el servidor

```bash
python manage.py runserver
```

Después se puede acceder a la aplicación desde:

```text
http://127.0.0.1:8000/
```

## Repositorio

Repositorio oficial del proyecto:

**https://github.com/BrandonSanjuan/SanjuanEnriquezBrandonAlexisUnidad2**

## Autor

**Brandon Alexis Sanjuan Enríquez**

Proyecto académico — Desarrollo Web Integral, Unidad 2.
