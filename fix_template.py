import os

file_path = r'c:\Users\JULI\Desktop\DyM cosmeticos\templates\catalogo\producto_list.html'

content = """{% extends 'base.html' %}

{% block content %}
<div class="bg-gray-100 py-8">
    <div class="container mx-auto px-4">
        <h1 class="text-3xl font-serif font-bold text-gray-800 mb-6 animate-fade-in-up">Catálogo de Productos</h1>

        <div class="flex flex-col lg:flex-row gap-8">
            <!-- Sidebar Filters -->
            <aside class="w-full lg:w-1/4 animate-fade-in-up" style="animation-delay: 0.1s;">
                <div class="bg-white p-6 rounded-lg shadow-sm sticky top-24">
                    <h3 class="font-bold text-lg mb-4 border-b pb-2">Filtrar por</h3>

                    <form action="." method="get">
                        <!-- Search -->
                        <div class="mb-6">
                            <input type="text" name="q" value="{{ search_query|default:'' }}"
                                placeholder="Buscar producto..."
                                class="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-dym-accent">
                        </div>

                        <!-- Brands -->
                        <div class="mb-6">
                            <h4 class="font-medium mb-3 text-sm uppercase text-gray-500">Marcas</h4>
                            <div class="space-y-2 max-h-60 overflow-y-auto">
                                <label class="flex items-center gap-2 cursor-pointer hover:text-dym-accent">
                                    <input type="radio" 
                                           name="marca" 
                                           value="" 
                                           {% if not current_marca %}checked{% endif %} 
                                           onchange="this.form.submit()" 
                                           class="text-dym-accent focus:ring-dym-accent">
                                    <span class="text-sm">Todas</span>
                                </label>
                                {% for m in marcas %}
                                <label class="flex items-center gap-2 cursor-pointer hover:text-dym-accent">
                                    <input type="radio" 
                                           name="marca" 
                                           value="{{ m.slug }}" 
                                           {% if current_marca == m.slug %}checked{% endif %} 
                                           onchange="this.form.submit()" 
                                           class="text-dym-accent focus:ring-dym-accent">
                                    <span class="text-sm">{{ m.nombre }}</span>
                                </label>
                                {% endfor %}
                            </div>
                        </div>

                        <!-- Categories -->
                        <div class="mb-6">
                            <h4 class="font-medium mb-3 text-sm uppercase text-gray-500">Categorías</h4>
                            <div class="space-y-2">
                                <label class="flex items-center gap-2 cursor-pointer hover:text-dym-accent">
                                    <input type="radio" 
                                           name="categoria" 
                                           value="" 
                                           {% if not current_categoria %}checked{% endif %} 
                                           onchange="this.form.submit()" 
                                           class="text-dym-accent focus:ring-dym-accent">
                                    <span class="text-sm">Todas</span>
                                </label>
                                {% for c in categorias %}
                                <label class="flex items-center gap-2 cursor-pointer hover:text-dym-accent">
                                    <input type="radio" 
                                           name="categoria" 
                                           value="{{ c.slug }}" 
                                           {% if current_categoria == c.slug %}checked{% endif %} 
                                           onchange="this.form.submit()" 
                                           class="text-dym-accent focus:ring-dym-accent">
                                    <span class="text-sm">{{ c.nombre }}</span>
                                </label>
                                {% endfor %}
                            </div>
                        </div>

                        {% if current_marca or current_categoria or search_query %}
                        <a href="{% url 'catalogo:producto_list' %}"
                            class="block w-full text-center text-sm text-red-500 hover:text-red-700 mt-4">
                            Limpiar Filtros
                        </a>
                        {% endif %}
                    </form>
                </div>
            </aside>

            <!-- Product Grid -->
            <div class="w-full lg:w-3/4 animate-fade-in-up" style="animation-delay: 0.2s;">
                {% if page_obj %}
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    {% for producto in page_obj %}
                    <!-- Gradient Border Wrapper -->
                    <div class="rounded-lg p-[1px] bg-gradient-to-br from-dym-accent to-pink-200 hover:from-pink-400 hover:to-dym-accent transition-all duration-500 shadow-sm hover:shadow-lg group">
                        <div class="bg-white rounded-lg h-full flex flex-col overflow-hidden">
                            <div class="relative aspect-square overflow-hidden bg-gray-50">
                                {% if producto.imagen_principal %}
                                <img src="{{ producto.imagen_principal.url }}" alt="{{ producto.nombre }}"
                                    class="w-full h-full object-cover hover:scale-105 transition duration-500">
                                {% else %}
                                <div class="w-full h-full flex items-center justify-center text-gray-400">Sin Imagen
                                </div>
                                {% endif %}
                                <!-- Quick View Overlay -->
                                <div class="absolute inset-0 bg-black bg-opacity-10 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center">
                                     <span class="bg-white text-dym-dark px-4 py-2 rounded-full font-bold text-sm shadow-lg transform scale-90 group-hover:scale-100 transition">Ver Detalle</span>
                                </div>
                            </div>
                            <div class="p-4 flex-grow flex flex-col">
                                <p class="text-xs text-dym-accent font-bold uppercase mb-1">{{ producto.marca.nombre }}
                                </p>
                                <h3 class="font-bold text-gray-800 mb-2">{{ producto.nombre }}</h3>
                                <div class="mt-auto pt-4">
                                    <a href="{% url 'catalogo:producto_detail' producto.slug %}"
                                        class="block w-full text-center border border-dym-dark text-dym-dark py-2 rounded hover:bg-dym-dark hover:text-white transition text-sm font-medium">
                                        Ver Detalle
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>

                <!-- Pagination -->
                <div class="mt-8 flex justify-center gap-2">
                    {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}{% if current_marca %}&marca={{ current_marca }}{% endif %}{% if current_categoria %}&categoria={{ current_categoria }}{% endif %}{% if search_query %}&q={{ search_query }}{% endif %}"
                        class="px-3 py-1 border rounded hover:bg-gray-100">Anterior</a>
                    {% endif %}

                    <span class="px-3 py-1">Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}</span>

                    {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}{% if current_marca %}&marca={{ current_marca }}{% endif %}{% if current_categoria %}&categoria={{ current_categoria }}{% endif %}{% if search_query %}&q={{ search_query }}{% endif %}"
                        class="px-3 py-1 border rounded hover:bg-gray-100">Siguiente</a>
                    {% endif %}
                </div>

                {% else %}
                <div class="text-center py-20 bg-white rounded-lg shadow-sm">
                    <p class="text-gray-500 text-lg">No se encontraron productos con esos filtros.</p>
                    <a href="{% url 'catalogo:producto_list' %}" class="text-dym-accent font-bold mt-2 inline-block">Ver
                        todo el catálogo</a>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File overwritten successfully at {file_path}")
