from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProxy


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ('email', 'name', 'bio', 'country', 'city', 'age')
    list_display = ('id','email', 'name','is_staff', 'is_active', 'date_joined', 'date_updated', 'country', 'city',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'age', 'bio', 'country', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'bio', 'country', 'city','age', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class UserProxyAdminPanel(admin.ModelAdmin):
    readonly_fields = ('user', 'session')
    list_display = ('id', 'user', 'session')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProxy, UserProxyAdminPanel)
