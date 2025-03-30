# Subida de Archivos a Amazon S3 con Python

Este proyecto permite subir archivos a un bucket de Amazon S3 utilizando **boto3**. Puedes optar por crear un nuevo bucket o usar uno existente. Se asegura el manejo seguro de las credenciales mediante variables de entorno o un archivo `.env`, evitando la inclusión directa de claves en el código.

---

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
  - [1. Clonar el Repositorio o Descargar el Script](#1-clonar-el-repositorio-o-descargar-el-script)
  - [2. Crear y Activar un Entorno Virtual](#2-crear-y-activar-un-entorno-virtual)
  - [3. Instalar Dependencias](#3-instalar-dependencias)
- [Configuración de Credenciales de AWS](#configuración-de-credenciales-de-aws)
  - [En Linux/macOS](#en-linuxmacos)
  - [En Windows](#en-windows)
  - [Verificar la Configuración](#verificar-la-configuración)
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
bash
Copiar
python -m venv venv

En Windows:

bash
Copiar
venv\Scripts\activate

En Linux/macOS:

bash
Copiar
source venv/bin/activate

Verifica que el prompt de la terminal muestre (venv).

Instalar Dependencias
Con el entorno virtual activado, instala las librerías necesarias:

bash
Copiar
pip install boto3 python-dotenv

Configuración de Credenciales de AWS
Para garantizar la seguridad, no debes hardcodear tus claves en el código.
En su lugar, configura tus credenciales mediante variables de entorno.

En Linux/macOS
Añade las siguientes líneas a tu archivo de configuración (por ejemplo, ~/.bashrc o ~/.zshrc):

bash
Copiar
export AWS_ACCESS_KEY_ID="TU_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="TU_SECRET_KEY"
export AWS_REGION="us-east-1" # Cambia por la región deseada

Luego, carga los cambios:

bash
Copiar
source ~/.bashrc

En Windows (CMD o PowerShell)
Ejecuta estos comandos para establecer las variables de entorno:

bash
Copiar
setx AWS_ACCESS_KEY_ID "TU_ACCESS_KEY"
setx AWS_SECRET_ACCESS_KEY "TU_SECRET_KEY"
setx AWS_REGION "us-east-1"

Verificar la Configuración
Linux/macOS:

bash
Copiar
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
echo $AWS_REGION

Windows:

bash
Copiar
echo %AWS_ACCESS_KEY_ID%
echo %AWS_SECRET_ACCESS_KEY%
echo %AWS_REGION%

Nota: Alternativamente, puedes crear un archivo .env en el directorio del proyecto con el siguiente contenido, y asegurarte de agregarlo a .gitignore:

ini
Copiar
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=us-east-1

Cómo Ejecutar el Script
Asegúrate de que el entorno virtual esté activo
(el prompt debe mostrar (venv)).

Ejecuta el script:

bash
Copiar
python upload_to_s3.py

Sigue las Instrucciones:

Se te preguntará si deseas crear un nuevo bucket o usar uno existente.

Si eliges crear un bucket, ingresa el nombre deseado.

Luego, ingresa la ruta del archivo a subir (sin comillas).

Ejemplo de Uso
Al ejecutar el script, la terminal mostrará algo similar a lo siguiente:

plaintext
Copiar
¿Quieres crear un nuevo bucket o usar uno existente? (crear/usar): crear
Ingresa el nombre del nuevo bucket: mi-bucket-prueba
Bucket 'mi-bucket-prueba' creado exitosamente en la región 'us-east-1'.
Ingresa la ruta del archivo a subir: /home/user/documento.pdf
Archivo 'documento.pdf' subido exitosamente a 'mi-bucket-prueba'.

Validación de la Carga
Para confirmar que el archivo se ha subido correctamente, revisa el contenido del bucket en la consola de AWS S3. Deberías ver el archivo subido con el nombre especificado.

Posibles Errores y Soluciones

Error	Causa Posible	Solución
No se encontraron credenciales de AWS	Variables de entorno no configuradas	Verifica la configuración con echo $AWS_ACCESS_KEY_ID
El archivo no existe	Ruta incorrecta del archivo	Usa la ruta completa del archivo sin comillas
El bucket ya existe y es de otra cuenta	Nombre de bucket ya en uso	Usa un nombre único o selecciona otro bucket
Error de permisos o conexión	Problemas de red o configuración IAM	Revisa tu conexión y asegúrate de que los permisos sean correctos
Licencia y Créditos

Licencia:
Este proyecto se distribuye bajo la Licencia MIT.

Créditos:
Desarrollado en Python utilizando la librería boto3.
Basado en las mejores prácticas de seguridad para el manejo de credenciales en AWS.
