from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_key')
    role = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'user_role'
