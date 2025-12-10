# Distribuidora DyM - Sitio Web

Este proyecto es la base para el sitio web de **Distribuidora DyM**, un catálogo de cosmética capilar profesional desarrollado en Django.

## 🚀 Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1. Crear entorno virtual
Es recomendable usar un entorno virtual para aislar las dependencias.

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones
Esto creará la base de datos `db.sqlite3` con las tablas necesarias.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear Superusuario
Para acceder al panel de administración (/admin), necesitás un usuario administrador.

```bash
python manage.py createsuperuser
```
Sigue las instrucciones para elegir nombre de usuario y contraseña.

### 5. Correr el servidor
```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` en tu navegador.
Para el admin, visita `http://127.0.0.1:8000/admin/`.

## ⚙️ Configuración Inicial (Admin)

Una vez logueado en el admin, te recomendamos hacer lo siguiente para que el sitio se vea bien:

1. **Configuración del Sitio**:
   - Ve a "Configuración del Sitio" y crea un registro (solo permite uno).
   - Carga el número de WhatsApp (formato internacional, e.g., `54911...`).
   - Carga la URL de tu tienda de Mercado Libre.
   - Carga el logo si lo tenés.

2. **Cargar Datos**:
   - Crea algunas **Marcas** con sus logos.
   - Crea **Categorías** (Alisados, Shampoo, etc.).
   - Carga **Productos** asignándoles marca y categorías. Marca algunos como "Destacado" para que salgan en la Home.

## 🎨 Frontend y Diseño

El sitio utiliza **Tailwind CSS**.
En esta versión de desarrollo, estamos usando el script CDN de Tailwind en `base.html` para prototipado rápido.
> **Nota**: Para producción, se recomienda instalar Tailwind vía npm y compilar los estilos.

Los colores principales están definidos en la configuración de Tailwind en `base.html` y toman valores de la base de datos si se configuran en `SiteConfig`.

## 📂 Estructura del Proyecto

- `dym_project/`: Configuración principal de Django.
- `catalogo/`: App principal.
    - `models.py`: Definición de productos, marcas, etc.
    - `views.py`: Lógica de las páginas.
    - `urls.py`: Rutas del sitio.
- `templates/`: Archivos HTML.
- `static/`: Archivos estáticos (CSS, JS, imágenes del theme).
- `media/`: Archivos subidos por el usuario (fotos de productos).

---
**Desarrollado por el Equipo DyM AI (ARQ_Bro, FS_Bro, et al.)**
