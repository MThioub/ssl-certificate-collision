from django.contrib import admin

# Register your models here.

from .models import (
User,
Ip_adress
)

admin.site.register(User)
admin.site.register(Ip_adress)
