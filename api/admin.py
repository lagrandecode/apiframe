from django.contrib import admin

# Register your models here.

from .models import ApiModel

admin.site.register(ApiModel)
