from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User


@receiver(user_logged_in) #сигнал о том, что создан админ
def create_superuser_handler(sender, request, user, **kwargs):
    if user.is_superuser:
        pass


@receiver(post_save, sender='Olga_Model') #сигнал о том, что создан пост
def create_record_handler(sender, instance, created, **kwargs):
    if created:
        pass


@receiver(post_delete, sender='Olga_Model') #сигнал о том, что пост удален
def delete_record_handler(sender, instance, **kwargs):
    pass
