from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserCustomer, UserVendor


class CustomUserAdmin(UserAdmin):
    list_display      = ('username','email','role','first_name','last_name','is_active')
    ordering          = ('-date_joined',)
    filter_horizontal = ()
    list_filter       = ()
    fieldsets         = ()
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('email','username', 'password1', 'password2', 'role'),
                },
            ),
        )



class VendorAdmin(admin.ModelAdmin):
    list_display            = ('user','vendor_name','is_approved','created_at')
    list_display_links      = ('user','vendor_name')
    list_editable           = ('is_approved',)

class CustomerAdmin(admin.ModelAdmin):
    list_display            = ('user','created_at')
    list_display_links      = ('user',)



admin.site.register(User,CustomUserAdmin)
admin.site.register(UserVendor,VendorAdmin)
admin.site.register(UserCustomer,CustomerAdmin)
