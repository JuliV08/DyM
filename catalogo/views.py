from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Producto, Marca, CategoriaProducto

def home(request):
    """
    Pagina principal.
    Muestra Hero, Marcas, Productos Destacados.
    """
    productos_destacados = Producto.objects.filter(es_destacado=True).select_related('marca')[:4]
    marcas = Marca.objects.all().order_by('orden')[:6] # Solo mostrar algunas en home
    
    return render(request, 'catalogo/home.html', {
        'productos_destacados': productos_destacados,
        'marcas': marcas,
    })

def producto_list(request):
    """
    Catálogo completo con filtros.
    """
    productos = Producto.objects.all().select_related('marca').prefetch_related('categorias')
    
    # Filtros
    marca_slug = request.GET.get('marca')
    categoria_slug = request.GET.get('categoria')
    search = request.GET.get('q')

    if marca_slug:
        productos = productos.filter(marca__slug=marca_slug)
    if categoria_slug:
        productos = productos.filter(categorias__slug=categoria_slug)
    if search:
        productos = productos.filter(Q(nombre__icontains=search) | Q(descripcion_corta__icontains=search))

    # Paginación
    paginator = Paginator(productos, 12) # 12 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Contexto para los selectores de filtro
    marcas = Marca.objects.all()
    categorias = CategoriaProducto.objects.all()

    return render(request, 'catalogo/producto_list.html', {
        'page_obj': page_obj,
        'marcas': marcas,
        'categorias': categorias,
        'current_marca': marca_slug,
        'current_categoria': categoria_slug,
        'search_query': search
    })

def producto_detail(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    # Productos relacionados (misma marca o misma categoria)
    relacionados = Producto.objects.filter(marca=producto.marca).exclude(id=producto.id)[:4]
    
    return render(request, 'catalogo/producto_detail.html', {
        'producto': producto,
        'relacionados': relacionados
    })

def marca_list(request):
    marcas = Marca.objects.all()
    return render(request, 'catalogo/marca_list.html', {'marcas': marcas})

def marca_detail(request, slug):
    marca = get_object_or_404(Marca, slug=slug)
    productos = Producto.objects.filter(marca=marca)
    return render(request, 'catalogo/marca_detail.html', {
        'marca': marca,
        'productos': productos
    })

def nosotros(request):
    return render(request, 'catalogo/nosotros.html')
