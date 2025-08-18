# -*- coding: utf-8 -*-
import sys
import base64
import os
import subprocess

def instalar_librerias():
    """
    Verifica e instala las librerías necesarias si no están presentes.
    """
    print("Verificando librerías necesarias...")
    try:
        import PIL
        print("Librería Pillow encontrada.")
    except ImportError:
        print("Librería Pillow no encontrada. Instalando...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
            print("Pillow instalada con éxito.")
        except subprocess.CalledProcessError as e:
            print(f"Error al intentar instalar Pillow: {e}")
            sys.exit(1)

def convertir_a_base64(ruta_imagen):
    """
    Convierte una imagen a una cadena de texto codificada en base64.
    """
    extensiones_permitidas = ['.png', '.jpg', '.jpeg', '.webp']
    
    _, extension = os.path.splitext(ruta_imagen)
    
    if extension.lower() not in extensiones_permitidas:
        print(f"Error: Tipo de archivo no admitido. Se admiten {', '.join(extensiones_permitidas)}")
        return None, None
        
    try:
        with open(ruta_imagen, "rb") as archivo_imagen:
            bytes_imagen = archivo_imagen.read()
            codigo_base64 = base64.b64encode(bytes_imagen)
            return codigo_base64.decode('utf-8'), extension.lower()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_imagen}' no fue encontrado.")
        return None, None
    except Exception as e:
        print(f"Ocurrió un error inesperado al procesar la imagen: {e}")
        return None, None

def guardar_base64_en_archivo(nombre_archivo_salida, codigo_base64):
    """
    Guarda la cadena base64 en un nuevo archivo de texto.
    """
    try:
        with open(nombre_archivo_salida, "w", encoding='utf-8') as archivo_salida:
            archivo_salida.write(codigo_base64)
        print(f"Éxito: El contenido base64 ha sido guardado en '{nombre_archivo_salida}'")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo de salida: {e}")
        return False

def main():
    """
    Función principal del script.
    """
    # Instalar librerías al inicio
    instalar_librerias()

    # Verificar si se proporcionó un único argumento (el nombre del archivo)
    if len(sys.argv) != 2:
        print("Uso: python itobase64.py <nombre_del_archivo_de_imagen>")
        sys.exit(1)

    # El primer argumento es el nombre del script, el segundo es la ruta del archivo
    ruta_imagen = sys.argv[1]

    print(f"Procesando el archivo: {ruta_imagen}")

    # Convertir la imagen a base64 y obtener su tipo
    codigo_base64, extension_original = convertir_a_base64(ruta_imagen)

    # Si la conversión no fue exitosa, salir
    if not codigo_base64:
        sys.exit(1)
    
    # Construir el nombre del archivo de salida
    nombre_base, _ = os.path.splitext(os.path.basename(ruta_imagen))
    nombre_archivo_salida = f"{nombre_base}.base64"

    # Guardar el resultado en el archivo de texto
    if not guardar_base64_en_archivo(nombre_archivo_salida, codigo_base64):
        sys.exit(1)

if __name__ == "__main__":
    main()