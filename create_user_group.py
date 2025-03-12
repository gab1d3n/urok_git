import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

def create_group():
    group_name = "User Managers"
    group, created = Group.objects.get_or_create(name=group_name)

    User = get_user_model()
    content_type = ContentType.objects.get_for_model(User)

    permissions = Permission.objects.filter(content_type=content_type)
    group.permissions.set(permissions)

    print(f"Группа '{group_name}' создана и права назначены.")

    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        user.groups.add(group)
        print(f"Добавлен {user.username} в группу {group_name}.")

if __name__ == "__main__":
    create_group()
