"""
Script para verificar los datos migrados
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dym_project.settings')
django.setup()

from catalogo.models import Producto, Marca, CategoriaProducto, SiteConfig

print("=" * 50)
print("VERIFICACIÓN DE DATOS MIGRADOS A POSTGRESQL")
print("=" * 50)
print(f"✅ Marcas: {Marca.objects.count()}")
print(f"✅ Productos: {Producto.objects.count()}")
print(f"✅ Categorías: {CategoriaProducto.objects.count()}")
print(f"✅ SiteConfig: {SiteConfig.objects.count()}")
print("=" * 50)

# Mostrar algunas marcas
print("\nMarcas cargadas:")
for marca in Marca.objects.all()[:5]:
    print(f"  - {marca.nombre}")

print("\nProductos cargados (primeros 5):")
for producto in Producto.objects.all()[:5]:
    print(f"  - {producto.nombre} ({producto.marca.nombre})")
