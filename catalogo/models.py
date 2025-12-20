from django.db import models
from django.utils.text import slugify

class SiteConfig(models.Model):
    """
    Singleton-like model to store global site configuration.
    """
    whatsapp_number = models.CharField(max_length=20, help_text="Formato internacional sin + (ej: 5491112345678)")
    instagram_url = models.URLField(blank=True, null=True)
    mercado_libre_url = models.URLField(blank=True, null=True)
    email_contacto = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    horarios = models.TextField(blank=True, null=True, help_text="Ej: Lunes a Viernes de 9 a 18hs")
    logo_sitio = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="Logo Principal")
    logo_sitio_2 = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="Logo Secundario", help_text="Logo de cuenta asociada (se mostrará al lado del principal)")
    
    # Custom colors if needed
    primary_color = models.CharField(max_length=7, default='#000000', help_text="Hex code (ej: #FF00FF)")
    secondary_color = models.CharField(max_length=7, default='#FFFFFF')

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuración del Sitio"

    def __str__(self):
        return "Configuración DyM"

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    logo = models.ImageField(upload_to='marcas/')
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    imagen_referencia = models.ImageField(upload_to='categorias/', blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    categorias = models.ManyToManyField(CategoriaProducto, related_name='productos')
    descripcion_corta = models.CharField(max_length=255)
    descripcion_larga = models.TextField(blank=True)
    imagen_principal = models.ImageField(upload_to='productos/')
    es_destacado = models.BooleanField(default=False)
    tiene_stock = models.BooleanField(default=True, verbose_name="Tiene Stock", help_text="Desmarcar si el producto está sin stock")
    orden = models.IntegerField(default=0)
    
    # External Links
    url_mercado_libre = models.URLField(blank=True, null=True, help_text="Link al producto en ML. Si está vacío, se usará el de SiteConfig.")
    url_instagram = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='galeria')
    imagen = models.ImageField(upload_to='productos/galeria/')
    orden = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Imágenes de Galería"
        ordering = ['orden']
