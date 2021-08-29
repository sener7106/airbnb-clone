from django.contrib import admin
from . import models

# Register your models here.
# for our WebMaster

# decorator
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
