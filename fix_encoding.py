"""
Script para convertir data.json a UTF-8
"""
import json

# Intentar leer con diferentes encodings
encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']

for encoding in encodings:
    try:
        with open('data.json', 'r', encoding=encoding) as f:
            content = f.read()
        print(f"✅ Archivo leído exitosamente con encoding: {encoding}")
        
        # Guardar como UTF-8
        with open('data_utf8.json', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Archivo guardado como data_utf8.json en UTF-8")
        break
    except UnicodeDecodeError as e:
        print(f"❌ Fallo con {encoding}: {e}")
        continue
