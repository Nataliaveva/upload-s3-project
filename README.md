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
#En VS Code, crea un archivo llamado upload_to_s3.py y pega el siguiente código:
import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

def upload_file_to_s3(file_path, bucket_name, s3_file_name=None):
    """
    Sube un archivo a un bucket de AWS S3.

    :param file_path: Ruta local del archivo a subir.
    :param bucket_name: Nombre del bucket S3 de destino.
    :param s3_file_name: Nombre con el que se guardará el archivo en S3 (opcional).
    :return: True si la carga es exitosa, False en caso contrario.
    """
    if s3_file_name is None:
        s3_file_name = os.path.basename(file_path)
    
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

    if not aws_access_key or not aws_secret_key:
        print("ERROR: Las credenciales de AWS no están configuradas correctamente en el .env.")
        return False

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )

    try:
        s3_client.upload_file(file_path, bucket_name, s3_file_name)
        print(f"El archivo '{file_path}' se ha subido exitosamente a '{bucket_name}/{s3_file_name}'.")
        return True
    except FileNotFoundError:
        print(f"ERROR: El archivo '{file_path}' no se encontró.")
    except NoCredentialsError:
        print("ERROR: Credenciales de AWS no disponibles.")
    except ClientError as e:
        print("ERROR: Falló la carga del archivo:", e)
    
    return False

if __name__ == "__main__":
    file_path = input("Ingresa la ruta del archivo a subir: ").strip()
    bucket_name = input("Ingresa el nombre del bucket S3: ").strip()
    upload_file_to_s3(file_path, bucket_name)
#Guarda el archivo.
#Configurar las Credenciales de AWS
**AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=us-east-1**
Uso del Script
Asegúrate de que el entorno virtual esté activado (debes ver (venv) en la terminal).

Abre la terminal integrada de VS Code.

Ejecuta el script con el siguiente comando:

bash
Copiar
python upload_to_s3.py
Cuando se te solicite, ingresa la ruta del archivo a subir (por ejemplo, imagen.jpg o la ruta completa) y el nombre del bucket S3 (por ejemplo, mi-bucket-s3-ejemplo).

Si la configuración es correcta, verás un mensaje en la terminal indicando que el archivo se subió exitosamente.

Integración con Git y GitHub
1. Inicializar Git en el Proyecto
Abre la terminal integrada en VS Code y asegúrate de estar en la carpeta del proyecto.

Inicializa Git con:

bash
Copiar
git init
Agrega los archivos al repositorio local:

bash
Copiar
git add .
Realiza el commit inicial:

bash
Copiar
git commit -m "Commit inicial: Agrega script de subida a S3 y configuración"
2. Conectar con un Repositorio en GitHub
Crea un repositorio en GitHub (por ejemplo, upload-s3-project).

Ve a GitHub y crea un nuevo repositorio.

Copia la URL del repositorio (HTTPS recomendado).

En la terminal de VS Code, agrega el remoto:

bash
Copiar
git remote add origin https://github.com/tu_usuario/upload-s3-project.git
Envía el commit al repositorio remoto:

bash
Copiar
git push -u origin master
Solución de Problemas Comunes
Error en la subida:

Verifica que la ruta del archivo es correcta y que el archivo existe.

Credenciales incorrectas:

Revisa el archivo .env para asegurarte de que las claves son correctas y no contienen espacios extra.

Problemas al hacer push a GitHub:

Asegúrate de que la URL remota es correcta y, si se requiere autenticación, usa un token de acceso personal.

Notas de Seguridad
No subas tus credenciales reales a GitHub:

Si tu repositorio es público, asegúrate de incluir el archivo .env en el archivo .gitignore.

Uso de Variables de Entorno:

Siempre utiliza archivos como .env para manejar tus credenciales y evita hardcodearlas en el código fuente.

Permisos IAM:

Para producción, restringe los permisos del usuario IAM a solo lo necesario.
