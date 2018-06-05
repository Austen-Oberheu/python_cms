from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page, PageContent, PageMenu, MenuLink
# Register your models here.

class PageContentAdmin(SummernoteModelAdmin):
    search_fields = ['page__page_title']
    list_display = ('page', 'short_description')
    summernote_fields = '__all__'

class MenuLinkDisplay(SummernoteModelAdmin):
    summernote_fields = '__all__'

class PageMenuAdmin(SummernoteModelAdmin):
   #search_fields = ['page_title']
    #list_display = ('page_title', 'pub_date')
    summernote_fields = '__all__'

class PageAdmin(SummernoteModelAdmin):
    search_fields = ['page_title']
    list_display = ('page_title', 'pub_date')
    summernote_fields = '__all__'

admin.site.register(Page, PageAdmin)
admin.site.register(PageContent, PageContentAdmin)
admin.site.register(PageMenu, PageMenuAdmin)
admin.site.register(MenuLink, MenuLinkDisplay)
