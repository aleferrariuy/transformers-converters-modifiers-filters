import sys
import os
import pandas as pd

def convertir_xlsx_a_csv(archivo_entrada, archivo_salida):
    """
    Lee un archivo Excel (.xlsx) y lo convierte a formato .csv,
    excluyendo el índice del DataFrame en el archivo de salida.
    """
    try:
        # Lee el archivo de Excel y lo carga en un DataFrame de pandas
        df_excel = pd.read_excel(archivo_entrada)
        
        # Guarda el DataFrame en un archivo CSV, sin el índice y con codificación UTF-8
        df_excel.to_csv(archivo_salida, index=False, encoding='utf-8')
        
        print(f"--- ¡Archivo convertido exitosamente! Resultado guardado en: {archivo_salida}")

    except FileNotFoundError:
        print(f"--- Error: El archivo de entrada '{archivo_entrada}' no fue encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"--- Ocurrió un error inesperado durante la conversión: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 1. Valida que se haya proporcionado el argumento correcto
    if len(sys.argv) != 2:
        print("--- Uso: python convertidor.py <archivo.xlsx>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]

    # 2. Valida que el archivo de entrada sea un .xlsx
    if not archivo_entrada.lower().endswith('.xlsx'):
        print("--- Error: El archivo de entrada debe tener la extensión .xlsx")
        sys.exit(1)
        
    # 3. Define el nombre del archivo de salida
    nombre_base = os.path.splitext(archivo_entrada)[0]
    archivo_salida = nombre_base + '.csv'
    
    # 4. Llama a la función que realiza la conversión
    convertir_xlsx_a_csv(archivo_entrada, archivo_salida)
