from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import os
        if os.environ.get("RUN_MAIN") != "true":
            return

        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                email="master@example.com",
                password="masterpassword",
                first_name="Master",
                last_name="User"
            )
            print("Master user created: master@example.com / masterpassword")