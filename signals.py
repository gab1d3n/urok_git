from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_migrate)
def create_user_group(sender, **kwargs):
    group, created = Group.objects.get_or_create(name='UserManager')

    if created:
        content_type = ContentType.objects.get_for_model(User)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)

    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        user.groups.add(group)
