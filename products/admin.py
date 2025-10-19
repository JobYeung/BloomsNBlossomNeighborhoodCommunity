from django.contrib import admin

from .models import Product
from django.forms import NumberInput
from django.db import models

class ProductAdmin(admin.ModelAdmin):
    list_display = 'id','title','flower_style','flower_type','is_published','florist'
    list_display_links = 'id','title'
    list_filter = 'florist',
    list_editable = 'is_published','flower_type'
    search_fields = 'title','flower_style','florist'
    list_per_page = 25
    ordering = ['-id']
    #prepopulated_fields = {'title':('title',)}
    formfield_overrides = {
        models.IntegerField: {
            'widget': NumberInput(attrs={'size':'10'})
        },
    }
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Product, ProductAdmin)
