from django.contrib import admin
from organizations.models import Organizations


class OrgAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['org_name', 'location']
    # list_filter = ['admin', 'active', 'staff']
    fieldsets = (
        (None, {'fields': ('org_name', 'location')}),
        # ('Personal info', {'fields': ()}),
        # ('Permissions', {'fields': ('admin', 'active', 'staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('org_name', 'location',)}
         ),
    )
    search_fields = ['org_name']
    ordering = ['org_name']
    filter_horizontal = ()


# Register your models here.
admin.site.register(Organizations, OrgAdmin)
