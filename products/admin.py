from django.contrib import admin
from .models import Product, Subject
from django.forms import NumberInput
from django.db import models
from django import forms
from taggit.forms import TagWidget
from django.contrib.admin.widgets import FilteredSelectMultiple

class ProductAdminForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=FilteredSelectMultiple(verbose_name='category',is_stacked=False,attrs={'row':'5'}),required=False,label='Select Category'
    )
    class Meta:
        modle = Product
        fields = [
            'florist','title','flower_type','flower_style','occasion','category','seasonal','description','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_published'
        ]
        widget = {
            'category':TagWidget(), 
        }

class ProductAdmin(admin.ModelAdmin):
    list_display = 'id','title','flower_style','flower_type','is_published','florist','tag_list'
    list_display_links = 'id','title'
    list_filter = ('florist','flower_style')
    list_editable = ('is_published','flower_type')
    search_fields = ('title','flower_style','florist')
    list_per_page = 25
    ordering = ['-id']
    #prepopulated_fields = {'title':('title',)}
    formfield_overrides = {
        models.IntegerField: {
            'widget': NumberInput(attrs={'size':'10'})
        },
    }
    show_facets = admin.ShowFacets.ALWAYS

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('category')
    
    def display_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    display_subjects.short_description = 'Category'

class SubjectAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = ("name",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Subject, SubjectAdmin)
