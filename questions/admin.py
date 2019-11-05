from django.contrib import admin
from . import models

admin.site.register(models.Author)
admin.site.register(models.Question)
admin.site.register(models.Tag)
# Register your models here.
