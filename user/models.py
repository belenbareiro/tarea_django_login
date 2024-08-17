from django.db import models  # type: ignore
from django.contrib.auth.models import AbstractUser  # type: ignore
from django.utils import timezone  # type: ignore

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=0)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Adding related_name to avoid clash
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name=("groups"),
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",  # Adding related_name to avoid clash
        blank=True,
        help_text=("Specific permissions for this user."),
        verbose_name=("user permissions"),
    )

    def __str__(self):
        return self.username
