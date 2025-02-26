from decouple import config

DB_HOST = config('DB_HOST', default='localhost')
DB_PORT = config('DB_PORT', default=5432, cast=int)
DB_NAME = config('DB_NAME', default='database')
DB_USER = config('DB_USER', default='postgres')
DB_PASSWORD = config('DB_PASSWORD', default='password')

APP_PORT = config('APP_PORT', default=8000, cast=int)
APP_DEBUG = config('APP_DEBUG', default=False, cast=bool)