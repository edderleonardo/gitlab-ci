import os
import dj_database_url
from dotenv import load_dotenv
from gitlabci.settings import BASE_DIR

load_dotenv()

DATABASES = {
    # heroku or docker
    'default': dj_database_url.config(engine='django_postgrespool')
} if os.environ.get('DATABASE_URL', '') else {
    # localhost
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}