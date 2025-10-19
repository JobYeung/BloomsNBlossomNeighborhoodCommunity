from django.contrib import admin

from .models import Florist

class FloristAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_mvp', 'hire_date', 'phone')
    list_display_links = ('name', 'email', 'phone')
    list_editable = ('is_mvp', )
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Florist, FloristAdmin)
