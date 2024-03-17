from django.contrib import admin
from account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'date_of_birth', 'active']
    list_filter = ['date_of_birth', 'active']
    search_fields = ['date_of_birth', 'user__username']
