from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "membership",
        "is_staff",
        "last_login",
        "date_joined",
    )

    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "membership",
                    "is_staff",
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
