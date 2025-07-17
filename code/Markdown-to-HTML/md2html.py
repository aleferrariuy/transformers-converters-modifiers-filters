import sys
import os
import markdown

def convertir_md_a_html(archivo_entrada, archivo_salida):
    """
    Lee un archivo Markdown, lo convierte a HTML y guarda el resultado
    en un archivo de salida.
    """
    try:
        # Abre y lee el contenido del archivo de entrada (.md)
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            texto_markdown = f.read()

        # Convierte el texto Markdown a HTML usando la biblioteca
        html = markdown.markdown(texto_markdown)

        # Escribe el HTML resultante en el archivo de salida (.out)
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"--- ¡Archivo procesado exitosamente! Resultado guardado en: {archivo_salida}")

    except FileNotFoundError:
        print(f"--- Error: El archivo '{archivo_entrada}' no fue encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"--- Ocurrió un error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 1. Verifica que se haya pasado un único argumento (el nombre del archivo)
    if len(sys.argv) != 2:
        print("--- Uso: python md2html.py <nombre_de_tu_archivo.md>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]

    # 2. Verifica que el archivo de entrada tenga la extensión .md
    if not archivo_entrada.lower().endswith('.md'):
        print("--- Error: El archivo de entrada debe ser un archivo .md")
        sys.exit(1)

    # 3. Crea el nombre del archivo de salida cambiando la extensión a .out
    nombre_base = os.path.splitext(archivo_entrada)[0]
    archivo_salida = nombre_base + '.out'

    # 4. Llama a la función principal para realizar la conversión
    convertir_md_a_html(archivo_entrada, archivo_salida)
