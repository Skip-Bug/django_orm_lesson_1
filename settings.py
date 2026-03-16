from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': getenv('ENGINE'),
        'HOST': getenv('HOST'),
        'PORT': getenv('PORT'),
        'NAME': getenv('NAME'),
        'USER': getenv('USER'),
        'PASSWORD': getenv('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
