from django.contrib import admin
from .models import *


# Register your models here.
#

class RoomAdmin(admin.ModelAdmin):
    list_display = ('topic', 'name', 'description')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'updated', 'created')


admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message, MessageAdmin)
admin.site.register(User)
