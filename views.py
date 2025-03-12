from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    print(f"Пользователь {user.username} вошёл в систему.")

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    print(f"Пользователь {user.username} вышел из системы.")
