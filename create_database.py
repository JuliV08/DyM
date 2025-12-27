"""
Script para crear la base de datos PostgreSQL
Ejecutar una sola vez antes de las migraciones
"""
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Conexión como superusuario postgres
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="manteca123"
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

# Verificar si la base de datos existe
cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'dym_cosmeticos'")
exists = cursor.fetchone()

if not exists:
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('dym_cosmeticos')))
    print("✅ Base de datos 'dym_cosmeticos' creada exitosamente!")
else:
    print("ℹ️  La base de datos 'dym_cosmeticos' ya existe.")

cursor.close()
conn.close()
