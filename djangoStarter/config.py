from django.conf import settings


def global_settings(request):
    return {
        'APP_NAME': 'Django Vue Starter'
    }
