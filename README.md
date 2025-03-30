# Subida de Archivos a Amazon S3 con Python

Este proyecto permite subir archivos a un bucket de Amazon S3 utilizando **boto3**. Puedes optar por crear un nuevo bucket o utilizar uno existente. Se asegura el manejo seguro de credenciales mediante variables de entorno, evitando la inclusión directa de claves en el código.

---

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Configuración de Credenciales de AWS](#configuración-de-credenciales-de-aws)
- [Cómo Ejecutar el Script](#cómo-ejecutar-el-script)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Validación de la Carga](#validación-de-la-carga)
- [Posibles Errores y Soluciones](#posibles-errores-y-soluciones)
- [Licencia y Créditos](#licencia-y-créditos)

---

## Requisitos Previos

Antes de ejecutar el script, asegúrate de cumplir con los siguientes requisitos:

- **Cuenta de AWS:** Debes tener una cuenta y configurar tus credenciales.
- **Python 3.7 o superior:** Se recomienda usar una versión reciente de Python.
- **Librerías de Python:**
  - `boto3` para interactuar con AWS S3.
  - `python-dotenv` (opcional, recomendado) para cargar las credenciales desde un archivo `.env`.

---

## Instalación y Configuración

### 1. Clonar el Repositorio o Descargar el Script

Puedes clonar este repositorio con Git o descargar el script directamente:

```bash
git clone https://github.com/tu_usuario/s3-uploader.git
cd s3-uploader

### 1. Clonar el Repositorio o Descargar el Script
### 2. Crear y Activar un Entorno Virtual
Es recomendable usar un entorno virtual para aislar las dependencias del proyecto:
```bash
python -m venv venv

En Windows:
```bash
Copiar
venv\Scripts\activate
En Linux/macOS:
```bash
Copiar
source venv/bin/activate
Verifica que el prompt de la terminal muestre (venv).

