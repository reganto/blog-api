from django.contrib import admin

from api import models


admin.site.register(models.Post)
admin.site.register(models.Comment)
