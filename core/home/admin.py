from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','notification','user','is_seen']

admin.site.register(Students)
admin.site.register(Images)
admin.site.register(Informations)