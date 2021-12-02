"""
    Конфиг со всеми скрытыми переменными окружения
"""

SECRET_KEY = 'django-insecure-a!6%d2r2$qbu9y*@t8y7we_&2mvo0-^3q*m9%8$2@(!!cxpzx6'

DB_CONNECTION_DATA = {
        'NAME': 'test_task',
        'USER': 'root',
        'PASSWORD': 'root',
        # 'HOST': 'db',
        # 'PORT': '5432',
        'HOST': '127.0.0.1',
        'PORT': '8083',
}
