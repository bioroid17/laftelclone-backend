from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User


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
            "유저 정보",
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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "name",
        "age_rating",
    )
