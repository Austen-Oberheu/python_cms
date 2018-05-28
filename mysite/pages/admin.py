from django.contrib import admin
from .models import Page, PageContent
# Register your models here.

class PageContentInLine(admin.TabularInline):
    model = PageContent
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['page_title']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [PageContentInLine]
    search_fields = ['page_title']
    list_display = ('page_title', 'pub_date')

admin.site.register(Page, PageAdmin)