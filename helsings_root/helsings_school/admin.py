from django.contrib import admin
from .models import Profile, Alumnus


class HelsAdmin(admin.ModelAdmin):
    list_display = ("first_name", 'email','mobile','password')
    ordering = ('first_name',)
    search_fields = ('first_name',)

# Register your models here.
admin.site.register(Profile)

admin.site.register(Alumnus)


