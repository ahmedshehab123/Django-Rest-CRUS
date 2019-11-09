from django.contrib import admin

# Register your models here.


from .models import Products,News
admin.site.register(Products)
admin.site.register(News)