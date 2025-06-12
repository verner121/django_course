from django.contrib import admin
from .models import Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name")
    search_fields = ("email", "full_name")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
    search_fields = ('subject', 'body')