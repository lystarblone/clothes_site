from django.contrib import admin

# Register your models here.
from .models import Stuff

@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "short_description", "slug", "price", "type", "collection", "time_create", "last_char"]
    list_filter = ["name", "price", "time_create"]
    search_fields = ["name", "description"]
    ordering = ["-time_create"]
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "time_create"
    list_editable = ("type",)
    list_display_links = ["name"]

    @admin.display(description="Short Description")
    def short_description(self, obj):
        return f"{obj.description[:80]}" if obj.description else ""

    @admin.display(description="Last char in name")
    def last_char(self, stuff: Stuff):
        return f"Last char in name is {stuff.name[-1]}"