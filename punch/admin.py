from django.contrib import admin
from punch.models import Employee, Skill, Role, Market

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("airbnb_id", "first_name", "last_name", "role", "skill", "market", "active")
    search_fields = ("airbnb_id", "first_name", "last_name", "role", "skill", "market", "active")


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class MarketAdmin(admin.ModelAdmin):
    list_display = ("language",)
    search_fields = ("language",)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Market, MarketAdmin)