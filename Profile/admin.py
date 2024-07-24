from django.contrib import admin
from .models import WatchOver
# Register your models here.

@admin.register(WatchOver)
class WatchOverAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'registered_at', 'Last_used']

    def get_username(self, obj):
        return obj.usr.username
    get_username.admin_order_field = 'user'
