from django.contrib import admin

# Register your models here.
from page.models import Category, Logo

admin.site.register(Category)
admin.site.register(Logo)