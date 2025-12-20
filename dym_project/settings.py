import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-example-key-replace-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Cámbialo a False cuando todo funcione bien

ALLOWED_HOSTS = ['*']

# Configuración necesaria para Railway y entornos seguros
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://adjunctly-unemitted-braiden.ngrok-free.dev', 
]

# Application definition
INSTALLED_APPS = [
    'jazzmin', # Jazzmin debe ir antes que el admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <--- FUNDAMENTAL PARA RAILWAY
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dym_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'catalogo.context_processors.site_config', 
            ],
        },
    },
]

WSGI_APPLICATION = 'dym_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES (Configuración para Producción) ---
STATIC_URL = 'static/'

# Esta carpeta DEBE existir en tu proyecto
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Carpeta donde Railway guardará los archivos para servirlos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Mejora el rendimiento de archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    "site_title": "Panel Cosméticos",
    "site_header": "Gestión de Productos",
    "site_brand": "Panel Admin",
    "welcome_sign": "Bienvenido al Sistema de Gestión",
    "copyright": "villeju",
    "search_model": ["auth.User", "catalogo.Producto", "catalogo.Marca", "catalogo.CategoriaProducto"],
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Ver Sitio Web", "url": "/", "new_window": True},
    ],
    "show_ui_builder": True,
}