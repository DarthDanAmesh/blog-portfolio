from django.contrib import admin
from .models import Wikis
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

##class PostAdmin(admin.ModelAdmin):
    
    #list_display = ('title', 'slug', 'status','created')
    #list_filter = ("status",)
    #search_fields = ['title', 'content']
    #prepopulated_fields = {'slug': ('title',)}

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
    summernote_fields = '__all__'

admin.site.register(Wikis, PostAdmin)