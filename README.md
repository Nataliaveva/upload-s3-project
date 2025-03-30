# Proyecto: Subida de Archivos a AWS S3 usando Python

Este proyecto contiene un script en Python que te permite subir archivos a un bucket de AWS S3. Además, el repositorio está versionado con Git y se ha integrado con GitHub, lo que te ayudará a aprender ambos conceptos. La guía es ideal para principiantes y explica cada paso detalladamente.

---

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Configuración de AWS](#configuración-de-aws)
- [Instalación y Configuración del Proyecto](#instalación-y-configuración-del-proyecto)
- [Uso del Script](#uso-del-script)
- [Integración con Git y GitHub](#integración-con-git-y-github)
- [Solución de Problemas Comunes](#solución-de-problemas-comunes)
- [Notas de Seguridad](#notas-de-seguridad)

---

## Requisitos

- **Cuenta en AWS:** Necesitas una cuenta en AWS para crear un bucket S3 y generar credenciales (usuario IAM).  
- **Python 3.x:** Asegúrate de tener Python instalado en tu sistema.  
- **Visual Studio Code (VS Code):** Se recomienda como entorno de desarrollo.  
- **Git:** Para controlar versiones y subir el proyecto a GitHub.  
- **Dependencias Python:**
  - `boto3` para interactuar con AWS S3.
  - `python-dotenv` para cargar variables de entorno desde un archivo `.env`.

---

## Configuración de AWS

### 1. Crear una Cuenta en AWS
- **Qué hacer:**  
  Si aún no tienes una cuenta, regístrate en [aws.amazon.com](https://aws.amazon.com/).

### 2. Configurar un Usuario IAM
- **Qué hacer:**  
  1. Ingresa a la Consola de AWS y abre el servicio **IAM**.  
  2. Crea un usuario nuevo, por ejemplo, `usuario-s3`.  
  3. Asigna permisos mínimos para S3. Para este ejemplo, puedes usar la política predefinida **AmazonS3FullAccess**.  
     *(En producción se recomienda restringir los permisos a lo estrictamente necesario).*

### 3. Crear un Bucket S3
- **Qué hacer:**  
  1. En la Consola de AWS, abre el servicio **S3**.  
  2. Haz clic en **Crear bucket**.  
  3. Asigna un nombre único al bucket, por ejemplo, `mi-bucket-s3-ejemplo`.  
  4. Selecciona la región deseada (por ejemplo, `us-east-1`) y sigue las instrucciones para finalizar la creación.

---

## Instalación y Configuración del Proyecto

### 1. Clonar o Crear el Proyecto en tu Computadora
- **Pasos a seguir:**  
  1. Crea una carpeta para el proyecto en tu sistema, por ejemplo, `upload_s3_project`.  
  2. Abre esta carpeta en Visual Studio Code.

### 2. Configurar un Entorno Virtual en Python
- **Pasos a seguir:**  
  1. Abre la **Terminal Integrada** en VS Code (Menú **Terminal > Nueva Terminal**).  
  2. Crea el entorno virtual ejecutando:
     ```bash
     python -m venv venv
     ```
  3. Activa el entorno virtual:
     - **En Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **En macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```
  4. Verifica que el prompt de la terminal muestre `(venv)` al inicio.

### 3. Instalar Dependencias
- **Pasos a seguir:**  
  Con el entorno virtual activado, instala las librerías necesarias ejecutando:
  ```bash
  pip install boto3 python-dotenv

### 4. Crear el Archivo del Script
- **Pasos a seguir:**  
  En VS Code, crea un archivo llamado upload_to_s3.py en la carpeta del proyecto.
  
### 5.  Configurar las Credenciales de AWS
- **Pasos a seguir:**  
  En la raíz del proyecto, crea un archivo llamado .env.
  ```bash
  AWS_ACCESS_KEY_ID=your_access_key_here
  AWS_SECRET_ACCESS_KEY=your_secret_key_here
  AWS_DEFAULT_REGION=us-east-1
