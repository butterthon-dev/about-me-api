from django.contrib import admin

from api.models.user import User


class UserAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(User, UserAdmin)
