# Proyecto: Subida de Archivos a AWS S3 usando Python

Este proyecto contiene un script en Python que te permite subir archivos a un bucket de AWS S3. Además, el repositorio está versionado con Git y se ha integrado con GitHub para que puedas aprender a usar ambos. La guía es ideal para principiantes y explica cada paso detalladamente.

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
- **Python 3.x:** Asegúrate de tener Python instalado.
- **Visual Studio Code (VS Code):** Se recomienda como entorno de desarrollo.
- **Git:** Para controlar versiones y subir el proyecto a GitHub.
- **Dependencias Python:**  
  - `boto3` para interactuar con AWS S3.  
  - `python-dotenv` para cargar variables de entorno desde un archivo `.env`.

---

## Configuración de AWS

1. **Crear una Cuenta en AWS:**  
   Si aún no tienes una cuenta, regístrate en [aws.amazon.com](https://aws.amazon.com/).

2. **Configurar un Usuario IAM:**  
   - Ingresa a la [Consola de AWS](https://aws.amazon.com/console/) y abre el servicio **IAM**.  
   - Crea un usuario nuevo (por ejemplo, `usuario-s3`) y asígnale permisos mínimos para S3.  
   - Para este ejemplo, puedes usar la política predefinida **AmazonS3FullAccess** (aunque para producción se recomienda restringir permisos).

3. **Crear un Bucket S3:**  
   - En la consola de AWS, abre el servicio **S3**.  
   - Haz clic en **Crear bucket** y asigna un nombre único (por ejemplo, `mi-bucket-s3-ejemplo`).  
   - Selecciona la región deseada (por ejemplo, `us-east-1`) y sigue las instrucciones para finalizar la creación.

---

## Instalación y Configuración del Proyecto

### 1. Clonar o Crear el Proyecto en tu Computadora

- Crea una carpeta para el proyecto (por ejemplo, `upload_s3_project`) en tu sistema.
- Abre la carpeta en Visual Studio Code.

### 2. Configurar un Entorno Virtual en Python

1. Abre la **Terminal Integrada** en VS Code:  
   - Menú **Terminal > Nueva Terminal**.

2. Crea y activa el entorno virtual:
   - **Crear entorno virtual:**
     ```bash
     python -m venv venv
     ```
   - **Activar entorno virtual:**  
     - En **Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - En **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

### 3. Instalar Dependencias

Con el entorno virtual activado, instala las librerías necesarias:
```bash
pip install boto3 python-dotenv
