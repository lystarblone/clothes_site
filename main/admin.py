from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Stuff, StuffImage, Collection, Type

@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "short_name", "short_description", "slug", "price", "type", "collection", "time_create", "first_photo"]
    list_filter = ["name", "price", "time_create"]
    search_fields = ["name", "description"]
    ordering = ["-time_create"]
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "time_create"
    list_editable = ("type", )
    list_display_links = ["name"]

    @admin.display(description="Short Description")
    def short_description(self, obj):
        return f"{obj.description[:80]}" if obj.description else ""

    @admin.display(description="Photo")
    def first_photo(self, stuff_image: StuffImage):
        first_image = stuff_image.images.first()
        if first_image:
                return format_html(
                    '<img src="{}" width="50" height="50" />', 
                    first_image.image.url
                )
        return "-"

@admin.register(StuffImage)
class StuffImageAdmin(admin.ModelAdmin):
    list_display = ["id", "stuff", "image_thumbnail"]

    @admin.display(description="Thumbnail")
    def image_thumbnail(self, obj):
        return format_html(
            '<img src="{}" width="50" height="50" />', 
            obj.image.url
        )
    
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "slug", "collection_image"]
    prepopulated_fields = {"slug": ("name",)}
     
    @admin.display(description="Image")
    def collection_image(self, collection_image: Collection):
        if collection_image.image:
                return format_html(
                    '<img src="{}" width="50" height="50" />', 
                    collection_image.image.url
                )
        return "-"
    
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]