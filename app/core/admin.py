from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models
from django.utils.translation import gettext as _


class UserAdmin(ModelAdmin):
    ordering = ['id', ]
    list_display = ('email', 'password')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'last_login', 'mama')
        }),
    )

admin.site.register(models.User, UserAdmin)
