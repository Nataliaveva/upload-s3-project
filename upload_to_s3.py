import boto3
import os
import sys
import re
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_s3_client():
    """
    Obtiene el cliente de S3 usando las credenciales de AWS desde variables de entorno.
    Asegura que las credenciales no estén hardcodeadas en el código.
    """
    try:
        return boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
    except (NoCredentialsError, PartialCredentialsError):
        print("❌ Error: No se encontraron credenciales de AWS. Asegúrate de configurarlas correctamente.")
        sys.exit(1)

def is_valid_bucket_name(bucket_name):
    """
    Verifica si el nombre del bucket es válido según las reglas de AWS S3.
    - Debe contener solo letras minúsculas, números, puntos y guiones.
    - Debe tener entre 3 y 63 caracteres.
    - No puede comenzar ni terminar con guiones o puntos.
    - No puede contener secuencias de caracteres como "--" o "..".
    """
    pattern = r"^(?![-.])[a-z0-9.-]{3,63}(?<![-.])$"
    return bool(re.match(pattern, bucket_name)) and "--" not in bucket_name and ".." not in bucket_name

def create_bucket(s3_client, bucket_name, region):
    """
    Crea un nuevo bucket en AWS S3 en la región especificada.
    En `us-east-1` no se requiere configuración adicional para la creación.
    """
    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"✅ Bucket '{bucket_name}' creado exitosamente en la región '{region}'.")
    except Exception as e:
        print(f"❌ Error al crear el bucket: {e}")
        sys.exit(1)

def upload_file_to_s3(s3_client, bucket_name, file_path):
    """
    Sube un archivo al bucket de S3 especificado.
    El nombre del archivo en S3 será el mismo que el nombre local.
    """
    try:
        file_name = os.path.basename(file_path)  # Extrae el nombre del archivo
        s3_client.upload_file(file_path, bucket_name, file_name)
        print(f"✅ Archivo '{file_name}' subido exitosamente a '{bucket_name}'.")
    except Exception as e:
        print(f"❌ Error al subir el archivo: {e}")
        sys.exit(1)

def main():
    """
    Punto de entrada del script. Permite al usuario:
    - Crear un bucket nuevo o seleccionar uno existente.
    - Elegir un archivo de su sistema y subirlo a S3.
    """
    s3_client = get_s3_client()
    region = os.getenv("AWS_REGION", "us-east-1")  # Si no está definida, usa "us-east-1"

    # Pregunta al usuario si quiere crear un bucket o usar uno existente
    choice = input("¿Quieres crear un nuevo bucket o usar uno existente? (crear/usar): ").strip().lower()
    
    if choice == "crear":
        while True:
            bucket_name = input("Ingresa el nombre del nuevo bucket: ").strip().lower()
            if is_valid_bucket_name(bucket_name):
                break
            print("⚠ El nombre del bucket no es válido. Inténtalo de nuevo.")
        
        create_bucket(s3_client, bucket_name, region)

    elif choice == "usar":
        bucket_name = input("Ingresa el nombre del bucket existente: ").strip()
    else:
        print("❌ Opción no válida.")
        sys.exit(1)

    # Validar la ruta del archivo antes de subirlo
    while True:
        file_path = input("Ingresa la ruta del archivo a subir (sin comillas): ").strip()
        if os.path.isfile(file_path):
            break
        print("⚠ Error: El archivo no existe. Inténtalo de nuevo.")

    upload_file_to_s3(s3_client, bucket_name, file_path)

if __name__ == "__main__":
    main()