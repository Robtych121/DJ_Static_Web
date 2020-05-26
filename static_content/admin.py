from django.contrib import admin
from .models import Static_Page

def publish_page(modeladmin, request, queryset):
    queryset.update(published='Yes')
    publish_page.short_description = "Publish Page"
    publish_page.allowed_permissions = ('change',)


def unpublish_page(modeladmin, request, queryset):
    queryset.update(published='No')
    unpublish_page.short_description = "Unpublish Page"
    unpublish_page.allowed_permissions = ('change',)


class StaticContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_date', 'published')
    actions = [publish_page,unpublish_page]


admin.site.register(Static_Page, StaticContentAdmin)