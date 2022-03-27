from django.contrib import admin
from .models import MyUser


class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'is_admin', 'is_active')
    list_editable = ['is_active']

    fieldsets = (
        (None, {'fields': ('full_name', 'is_admin', 'is_active')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'fields': (
    #             'password1', 'password2', 'full_name', 'is_admin', 'is_active')}
    #      ),
    # )

# Register your models here.
admin.site.register(MyUser, AdminUser)
