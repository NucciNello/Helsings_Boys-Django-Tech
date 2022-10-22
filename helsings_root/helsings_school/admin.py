from django.contrib import admin
from .models import Registered, Alumnus


class HelsAdmin(admin.ModelAdmin):
    list_display = ("first_name", 'email','mobile','password', 'date_created')
    ordering = ('first_name',)
    search_fields = ('first_name',)

# Register your models here.
admin.site.register(Registered)

admin.site.register(Alumnus)


