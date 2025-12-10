import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dym_project.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_initial_superuser():
    User = get_user_model()
    username = 'admin'
    email = 'admin@dym.com'
    password = 'admin'

    if not User.objects.filter(username=username).exists():
        print(f"Creando superusuario '{username}'...")
        User.objects.create_superuser(username, email, password)
        print(f"¡Listo! Usuario: {username} | Contraseña: {password}")
    else:
        print(f"El usuario '{username}' ya existe.")
        u = User.objects.get(username=username)
        u.set_password(password)
        u.save()
        print(f"Contraseña reseteada a '{password}' para el usuario '{username}'.")

if __name__ == '__main__':
    create_initial_superuser()
