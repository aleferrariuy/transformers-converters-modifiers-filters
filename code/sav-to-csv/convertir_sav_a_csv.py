# -*- coding: utf-8 -*-
"""
Script para convertir un archivo de datos de SPSS (.SAV) a un archivo CSV.
Recibe la ruta del archivo .SAV como único argumento desde la línea de comandos.
"""

import sys
import os
import pandas as pd
import pyreadstat

def convertir_sav_a_csv(ruta_archivo_sav):
    """
    Convierte un archivo .SAV a .CSV.

    Args:
        ruta_archivo_sav (str): La ruta completa al archivo .SAV de entrada.
    """
    # --- 1. Validar que el archivo de entrada exista ---
    if not os.path.exists(ruta_archivo_sav):
        print(f"--- Error: El archivo '{ruta_archivo_sav}' no fue encontrado.")
        return

    # --- 2. Validar que la extensión sea .sav ---
    if not ruta_archivo_sav.lower().endswith('.sav'):
        print(f"--- Error: El archivo proporcionado no es un archivo .SAV.")
        return

    # --- 3. Construir el nombre del archivo de salida ---
    # Se reemplaza la extensión .sav por .csv
    ruta_base = os.path.splitext(ruta_archivo_sav)[0]
    ruta_archivo_csv = ruta_base + ".csv"

    print(f"--- Convirtiendo '{ruta_archivo_sav}' a '{ruta_archivo_csv}'...")

    try:
        # --- 4. Leer el archivo .SAV usando pyreadstat ---
        # pyreadstat.read_sav devuelve un dataframe de pandas y un objeto de metadatos.
        # Solo necesitamos el dataframe, por eso usamos df, _
        df, meta = pyreadstat.read_sav(ruta_archivo_sav)

        # --- 5. Guardar el DataFrame como un archivo CSV ---
        # Se guarda en formato UTF-8 (compatible con la mayoría de los sistemas)
        # index=False evita que pandas escriba una columna extra con el índice del DataFrame.
        df.to_csv(ruta_archivo_csv, index=False, encoding='utf-8-sig')

        print(f"--- ¡Conversión completada con éxito!")
        print(f"--- El archivo resultante ha sido guardado en: {ruta_archivo_csv}")

    except Exception as e:
        print(f"--- Ocurrió un error inesperado durante la conversión: {e}")

# --- Punto de entrada del script ---
if __name__ == "__main__":
    # Se verifica que se haya pasado exactamente un argumento (el nombre del archivo).
    # sys.argv[0] es el nombre del script, sys.argv[1] es el primer argumento.
    if len(sys.argv) != 2:
        print("--- Uso incorrecto. Debe proporcionar la ruta a un archivo .SAV.")
        print(f"--- Ejemplo: python {sys.argv[0]} mis_datos.sav")
    else:
        # Se pasa el argumento de la línea de comandos a la función principal.
        archivo_origen = sys.argv[1]
        convertir_sav_a_csv(archivo_origen)
