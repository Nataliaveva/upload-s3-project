import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

# Cargar variables desde archivo .env
load_dotenv()

def get_s3_client():
    """Inicializa el cliente de S3 con credenciales desde variables de entorno"""
    try:
        aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

        if not aws_access_key or not aws_secret_key:
            print("❌ ERROR: Credenciales de AWS no encontradas. Verifica el archivo .env o tus variables de entorno.")
            return None

        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )
        return s3
    except Exception as e:
        print(f"❌ ERROR al inicializar cliente de S3: {e}")
        return None

def create_bucket(s3, bucket_name, region):
    """Crea un bucket en la región especificada"""
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"✅ Bucket '{bucket_name}' creado exitosamente en la región '{region}'.")
    except ClientError as e:
        print(f"❌ ERROR al crear el bucket: {e}")

def check_bucket_exists(s3, bucket_name):
    """Verifica si el bucket ya existe"""
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False

def upload_file(s3, bucket_name, file_path):
    """Sube el archivo especificado al bucket"""
    try:
        if not os.path.isfile(file_path):
            print("❌ ERROR: El archivo no existe o la ruta es inválida.")
            return

        file_name = os.path.basename(file_path)
        s3.upload_file(file_path, bucket_name, file_name)
        print(f"✅ Archivo '{file_name}' subido exitosamente al bucket '{bucket_name}'.")
    except NoCredentialsError:
        print("❌ ERROR: Credenciales no válidas o faltantes.")
    except ClientError as e:
        print(f"❌ ERROR al subir archivo: {e}")

def main():
    s3 = get_s3_client()
    if not s3:
        return

    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    opcion = input("¿Quieres crear un nuevo bucket o usar uno existente? (crear/usar): ").strip().lower()

    if opcion == 'crear':
        bucket_name = input("Ingresa el nombre del nuevo bucket: ").strip()
        if check_bucket_exists(s3, bucket_name):
            print("⚠️ El bucket ya existe. Puedes usarlo o cambiar el nombre.")
        else:
            create_bucket(s3, bucket_name, region)
    elif opcion == 'usar':
        bucket_name = input("Ingresa el nombre del bucket existente: ").strip()
        if not check_bucket_exists(s3, bucket_name):
            print("❌ ERROR: El bucket no existe o no tienes acceso.")
            return
    else:
        print("❌ ERROR: Opción no válida. Escribe 'crear' o 'usar'.")
        return

    file_path = input("Ingresa la ruta completa del archivo a subir: ").strip()
    upload_file(s3, bucket_name, file_path)

if __name__ == "__main__":
    main()

