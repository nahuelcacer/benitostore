from .settings import * 
import dj_database_url

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'inseguro-en-dev')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
PORT = int(os.environ.get("PORT", 8000))
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}