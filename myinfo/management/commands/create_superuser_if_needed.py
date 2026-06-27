from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the Django superuser from environment variables if it does not already exist."

    def handle(self, *args, **options):
        username = options.get("username") or self._env("DJANGO_SUPERUSER_USERNAME")
        email = options.get("email") or self._env("DJANGO_SUPERUSER_EMAIL", required=False)
        password = options.get("password") or self._env("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            raise CommandError(
                "DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD are required."
            )

        User = get_user_model()
        user, created = User.objects.get_or_create(username=username, defaults={"email": email or ""})

        changed = False
        if email and user.email != email:
            user.email = email
            changed = True

        if not user.is_staff:
            user.is_staff = True
            changed = True

        if not user.is_superuser:
            user.is_superuser = True
            changed = True

        user.set_password(password)
        changed = True

        if changed:
            user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created superuser '{username}'."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Updated superuser '{username}'."))

    def _env(self, key, required=True):
        import os

        value = os.environ.get(key, "").strip()
        if required and not value:
            return None
        return value or None
