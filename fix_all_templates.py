import os

# Fix marca_list.html
marca_content = '''{% extends 'base.html' %}

{% block content %}
<div class="bg-gradient-to-b from-gray-50 to-gray-100 py-12 min-h-screen">
    <div class="container mx-auto px-4">
        <div class="text-center mb-12 animate-fade-in-up">
            <h1 class="text-4xl md:text-5xl font-serif font-bold text-gray-800 mb-4">Nuestras Marcas</h1>
            <p class="text-gray-500 max-w-2xl mx-auto">Trabajamos con las mejores marcas de cosmetica capilar profesional</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for marca in marcas %}
            <a href="{% url 'catalogo:marca_detail' marca.slug %}" class="group animate-fade-in-up">
                <div class="rounded-2xl p-[2px] bg-gradient-to-br from-dym-accent via-pink-300 to-pink-200 hover:from-pink-400 hover:via-dym-accent hover:to-pink-300 transition-all duration-500 shadow-md hover:shadow-xl hover:-translate-y-2">
                    <div class="bg-white rounded-2xl p-8 flex flex-col items-center text-center h-full">
                        <div class="h-32 w-full flex items-center justify-center mb-6 relative">
                            {% if marca.logo %}
                            <img src="{{ marca.logo.url }}" alt="{{ marca.nombre }}" class="max-h-full max-w-full object-contain filter grayscale group-hover:grayscale-0 transition duration-500 group-hover:scale-110">
                            {% else %}
                            <span class="text-3xl font-serif font-bold text-gray-300 group-hover:text-dym-accent transition-colors duration-300">{{ marca.nombre }}</span>
                            {% endif %}
                        </div>
                        <h3 class="text-xl font-bold mb-3 text-gray-800 group-hover:text-dym-accent transition-colors duration-300">{{ marca.nombre }}</h3>
                        {% if marca.descripcion %}
                        <p class="text-gray-500 text-sm line-clamp-3 mb-6">{{ marca.descripcion }}</p>
                        {% endif %}
                        <span class="mt-auto inline-flex items-center gap-2 px-6 py-2 bg-gradient-to-r from-gray-800 to-gray-700 text-white rounded-full text-sm font-semibold group-hover:from-dym-accent group-hover:to-pink-400 transition-all duration-300 shadow-sm">Ver Productos<svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg></span>
                    </div>
                </div>
            </a>
            {% empty %}
            <div class="col-span-full text-center py-20">
                <div class="text-6xl mb-4">📦</div>
                <p class="text-gray-500 text-lg">Todavia no hay marcas cargadas.</p>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}'''

with open(r'c:\Users\JULI\Desktop\DyM cosmeticos\templates\catalogo\marca_list.html', 'w', encoding='utf-8') as f:
    f.write(marca_content)
print('marca_list.html corregido!')

# Fix home.html
home_content = '''{% extends 'base.html' %}

{% block content %}
<!-- Hero Section -->
<section class="relative bg-gradient-to-r from-gray-50 to-white py-20 animate-fade-in overflow-hidden">
    <canvas id="particles-canvas" class="absolute inset-0 w-full h-full z-0 opacity-40 pointer-events-none"></canvas>
    <div class="container mx-auto px-4 text-center animate-fade-in-up relative z-10">
        <h1 class="text-4xl md:text-6xl font-serif font-bold text-dym-dark mb-4 drop-shadow-sm">Cosmetica Capilar Profesional</h1>
        <p class="text-lg md:text-xl text-gray-600 mb-8 max-w-2xl mx-auto">Descubri las mejores marcas para el cuidado de tu cabello. Calidad de salon en tu hogar.</p>
        <div class="flex flex-col md:flex-row gap-4 justify-center">
            <a href="{% url 'catalogo:producto_list' %}" class="bg-dym-dark text-white px-8 py-3 rounded-full font-medium hover:bg-gray-800 hover:scale-105 transition transform shadow-lg">Ver Productos</a>
            {% if site_config.whatsapp_number %}
            <a href="https://wa.me/{{ site_config.whatsapp_number }}" target="_blank" class="bg-green-500 text-white px-8 py-3 rounded-full font-medium hover:bg-green-600 hover:scale-105 transition transform shadow-lg flex items-center justify-center gap-2"><span>Escribinos por WhatsApp</span></a>
            {% endif %}
        </div>
    </div>
</section>

<!-- Features Section -->
<section class="py-12 bg-white">
    <div class="container mx-auto px-4 grid md:grid-cols-3 gap-8 text-center">
        <div class="p-6 hover:translate-y-[-5px] transition duration-300">
            <div class="text-dym-accent text-4xl mb-4">★</div>
            <h3 class="font-bold text-xl mb-2">Productos Profesionales</h3>
            <p class="text-gray-500">Seleccionamos las mejores marcas del mercado para garantizar resultados.</p>
        </div>
        <div class="p-6 hover:translate-y-[-5px] transition duration-300">
            <div class="text-dym-accent text-4xl mb-4">♥</div>
            <h3 class="font-bold text-xl mb-2">Asesoramiento Personalizado</h3>
            <p class="text-gray-500">Te ayudamos a elegir el tratamiento ideal para tu tipo de cabello.</p>
        </div>
        <div class="p-6 hover:translate-y-[-5px] transition duration-300">
            <div class="text-dym-accent text-4xl mb-4">⚡</div>
            <h3 class="font-bold text-xl mb-2">Envios a todo el pais</h3>
            <p class="text-gray-500">Compra seguro a traves de Mercado Libre y recibilo en tu casa.</p>
        </div>
    </div>
</section>

<!-- Featured Brands -->
{% if marcas %}
<section class="py-16 bg-gray-50">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl font-serif font-bold text-center mb-12">Nuestras Marcas</h2>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-8 items-center">
            {% for marca in marcas %}
            <a href="{% url 'catalogo:marca_detail' marca.slug %}" class="group text-center">
                <div class="bg-white rounded-xl shadow-sm p-4 h-32 flex items-center justify-center group-hover:shadow-lg group-hover:-translate-y-1 transition duration-300 border border-transparent hover:border-dym-accent">
                    {% if marca.logo %}
                    <img src="{{ marca.logo.url }}" alt="{{ marca.nombre }}" class="max-h-full max-w-full object-contain filter grayscale group-hover:grayscale-0 transition duration-300">
                    {% else %}
                    <span class="font-bold text-gray-400 group-hover:text-gray-600 transition">{{ marca.nombre }}</span>
                    {% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
        <div class="text-center mt-10">
            <a href="{% url 'catalogo:marca_list' %}" class="text-dym-accent font-bold hover:underline">Ver todas las marcas →</a>
        </div>
    </div>
</section>
{% endif %}

<!-- Featured Products -->
{% if productos_destacados %}
<section class="py-16 container mx-auto px-4">
    <h2 class="text-3xl font-serif font-bold text-center mb-12">Productos Destacados</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        {% for producto in productos_destacados %}
        <div class="rounded-lg p-[1px] bg-gradient-to-br from-dym-accent to-pink-200 hover:from-pink-400 hover:to-dym-accent transition-all duration-500 shadow-sm hover:shadow-xl group hover:-translate-y-2">
            <div class="bg-white rounded-lg overflow-hidden h-full flex flex-col">
                <div class="relative aspect-square overflow-hidden bg-gray-50">
                    {% if producto.imagen_principal %}
                    <img src="{{ producto.imagen_principal.url }}" alt="{{ producto.nombre }}" class="w-full h-full object-cover group-hover:scale-110 transition duration-700 ease-in-out">
                    {% else %}
                    <div class="w-full h-full flex items-center justify-center text-gray-400">Sin Imagen</div>
                    {% endif %}
                    <div class="absolute inset-0 bg-black bg-opacity-10 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center">
                        <span class="bg-white text-dym-dark px-4 py-2 rounded-full font-bold text-sm shadow-lg transform scale-90 group-hover:scale-100 transition">Ver Detalles</span>
                    </div>
                </div>
                <div class="p-6 flex-grow flex flex-col">
                    <p class="text-xs text-dym-accent font-bold uppercase tracking-wide mb-1">{{ producto.marca.nombre }}</p>
                    <h3 class="font-bold text-lg mb-2 text-gray-800">{{ producto.nombre }}</h3>
                    <p class="text-sm text-gray-500 line-clamp-2 mb-4">{{ producto.descripcion_corta }}</p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="{% url 'catalogo:producto_detail' producto.slug %}" class="block w-full text-center border border-dym-dark text-dym-dark py-2 rounded hover:bg-dym-dark hover:text-white transition text-sm font-medium">Ver Detalles</a>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
{% endif %}

<script>
document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('particles-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let width, height;
    const particles = [];
    const particleCount = 50;
    function resize() {
        width = canvas.width = canvas.parentElement.offsetWidth;
        height = canvas.height = canvas.parentElement.offsetHeight;
    }
    window.addEventListener('resize', resize);
    resize();
    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 4 + 2;
            this.speedX = Math.random() * 0.5 - 0.25;
            this.speedY = Math.random() * 0.5 - 0.25;
            this.color = '#D8A7B1';
            this.alpha = Math.random() * 0.6 + 0.3;
        }
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            if (this.x > width) this.x = 0;
            if (this.x < 0) this.x = width;
            if (this.y > height) this.y = 0;
            if (this.y < 0) this.y = height;
        }
        draw() {
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    function animate() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => { p.update(); p.draw(); });
        requestAnimationFrame(animate);
    }
    animate();
});
</script>
{% endblock %}'''

with open(r'c:\Users\JULI\Desktop\DyM cosmeticos\templates\catalogo\home.html', 'w', encoding='utf-8') as f:
    f.write(home_content)
print('home.html corregido!')

print('\\n¡Todos los templates corregidos!')
