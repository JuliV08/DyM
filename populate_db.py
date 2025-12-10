import os
import django
from django.core.files.base import ContentFile

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dym_project.settings')
django.setup()

from catalogo.models import Marca, CategoriaProducto, Producto, SiteConfig
from django.utils.text import slugify

def populate():
    print("Creando datos de prueba...")

    # SiteConfig
    if not SiteConfig.objects.exists():
        SiteConfig.objects.create(
            whatsapp_number="5491112345678",
            instagram_url="https://instagram.com/distribuidoradym",
            mercado_libre_url="https://mercadolibre.com.ar",
            email_contacto="hola@dym.com",
            direccion="Av. Corrientes 1234, CABA"
        )
        print("- Configuración del sitio creada")

    # Categorias
    cat_alisados, _ = CategoriaProducto.objects.get_or_create(nombre="Alisados", slug="alisados")
    cat_shampoo, _ = CategoriaProducto.objects.get_or_create(nombre="Shampoo y Acondicionador", slug="shampoo")
    cat_tratamientos, _ = CategoriaProducto.objects.get_or_create(nombre="Tratamientos", slug="tratamientos")
    print("- Categorías creadas")

    # Marcas
    marca_fidely, _ = Marca.objects.get_or_create(
        nombre="Fidely", 
        defaults={'descripcion': 'Línea premium de alisados y tratamientos capilares.'}
    )
    marca_alfaparf, _ = Marca.objects.get_or_create(
        nombre="Alfaparf", 
        defaults={'descripcion': 'Excelencia italiana para el cuidado del cabello.'}
    )
    print("- Marcas creadas")

    # Productos
    prod1, _ = Producto.objects.get_or_create(
        nombre="Alisado Forte 1L",
        defaults={
            'marca': marca_fidely,
            'descripcion_corta': 'Alisado definitivo fuerza extra.',
            'descripcion_larga': 'Ideal para cabellos rebeldes. Dura 6 meses. Uso profesional.',
            'es_destacado': True,
            'orden': 1
        }
    )
    prod1.categorias.add(cat_alisados)

    prod2, _ = Producto.objects.get_or_create(
        nombre="Shampoo Ácido pH 4.5",
        defaults={
            'marca': marca_fidely,
            'descripcion_corta': 'Shampoo post-alisado para mantenimiento.',
            'es_destacado': False,
            'orden': 2
        }
    )
    prod2.categorias.add(cat_shampoo)

    prod3, _ = Producto.objects.get_or_create(
        nombre="Semi Di Lino Diamond",
        defaults={
            'marca': marca_alfaparf,
            'descripcion_corta': 'Cristales líquidos iluminadores.',
            'es_destacado': True,
            'orden': 3
        }
    )
    prod3.categorias.add(cat_tratamientos)

    print("- Productos de ejemplo creados")
    print("¡Base de datos poblada con éxito!")

if __name__ == '__main__':
    populate()
