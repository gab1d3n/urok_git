from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Создаёт группу User Managers и добавляет суперпользователей в неё"

    def handle(self, *args, **kwargs):
        group_name = "User Managers"
        group, created = Group.objects.get_or_create(name=group_name)

        User = get_user_model()
        content_type = ContentType.objects.get_for_model(User)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS(f"Группа '{group_name}' создана и права назначены."))

        superusers = User.objects.filter(is_superuser=True)
        for user in superusers:
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS(f"Добавлен {user.username} в группу {group_name}."))

