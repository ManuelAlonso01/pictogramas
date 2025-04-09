
# Web de Pictogramas

# Sistema de Pictogramas con Síntesis de Voz 🗣️🖼️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

Aplicación web para crear y gestionar pictogramas con funcionalidad de síntesis de voz, desarrollada con Flask y SQLite.

## Características Principales ✨
- Interfaz web interactiva
- Gestión de pictogramas (subir/borrar)
- Sistema de categorías
- Generación de oraciones con pictogramas
- Síntesis de voz integrada
- Persistencia de selecciones (localStorage)
- Paginación de resultados
- Gestión mediante base de datos SQLite

## Tecnologías Utilizadas 🛠️
- Python 3.8+
- Flask
- SQLite
- HTML5/CSS/JavaScript
- Web Speech API

## Instalación y Configuración ⚙️

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes Python)

### Pasos de Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/ManuelAlonso2006/pictogramas.git
cd pictogramas
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### Uso 🚀

1. Iniciar la aplicacion
```bash
python app.py
```

2. Accede a tu navegador
```bash
http://localhost:5000
```

### Funcionalidades Principales
Interfaz Principal:

    1)Visualizar pictogramas paginados

    2)Seleccionar imágenes para formar oraciones

    3)Reproducir oraciones con síntesis de voz

    4)Acceso a categorías

### Gestión:

    1)Subir/Borrar pictogramas

    2)Crear nuevas categorías

    3)Filtrar por categorías

### Persistencia:

    1)Las selecciones se mantienen entre sesiones

    2)Última oración generada almacenada localmente


## Desarrollado por ManuelAlonso2006 <img src="https://github.com/ManuelAlonso2006/pictogramas/blob/main/profile.png" alt="profile" width="25">
