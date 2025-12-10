from django.contrib import admin
from django.utils.html import format_html
from .models import Marca, CategoriaProducto, Producto, ImagenProducto, SiteConfig

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'mostrar_imagen', 'es_destacado', 'orden')
    list_filter = ('marca', 'categorias', 'es_destacado')
    search_fields = ('nombre', 'descripcion_corta', 'marca__nombre')
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [ImagenProductoInline]
    filter_horizontal = ('categorias',)
    list_editable = ('es_destacado', 'orden')
    ordering = ('orden', 'nombre')

    def mostrar_imagen(self, obj):
        if obj.imagen_principal:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.imagen_principal.url)
        return "-"
    mostrar_imagen.short_description = "Imagen"

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mostrar_logo', 'orden')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ('orden',)

    def mostrar_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.logo.url)
        return "-"
    mostrar_logo.short_description = "Logo"

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion
        return False
