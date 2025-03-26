from pathlib import Path
import os

# Định nghĩa thư mục gốc của project
BASE_DIR = Path(__file__).resolve().parent.parent

# Bảo mật Django
SECRET_KEY = 'django-insecure-9-gpyiy*hradypyc2s$=^rvil0k4o*my7(#_@uh(x3)9%e_h(5'

DEBUG = True  # TẮT DEBUG trong môi trường production

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Chỉnh sửa nếu deploy

# Cấu hình ứng dụng Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Ứng dụng của bạn
    'api',

    # Ứng dụng bên thứ ba
    'rest_framework',
    'corsheaders',
    'frontend'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Thêm middleware CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS - Cho phép truy cập API từ frontend khác domain
CORS_ALLOW_ALL_ORIGINS = True  # Nếu bạn chỉ muốn một số domain cụ thể, dùng `CORS_ALLOWED_ORIGINS`

ROOT_URLCONF = 'longbong.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Nếu dùng template, có thể thêm đường dẫn vào đây
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'longbong.wsgi.application'

# Cấu hình DATABASE (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'badminton',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}

# Cấu hình Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
   'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny',
]
    
}

# Cấu hình xác thực mật khẩu
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Ngôn ngữ & Múi giờ
LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True

# Cấu hình static & media files
STATIC_URL = '/static/'
STATICFILES_DIRS =[ BASE_DIR / 'frontend' / 'build' / 'static',]  # Nếu bạn có thư mục static
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Lưu file upload trong thư mục media

# Thiết lập trường khóa chính mặc định
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
