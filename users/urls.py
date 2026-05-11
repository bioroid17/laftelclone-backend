from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_pk>/", views.UserDetail.as_view(), name="user_detail"),
]
