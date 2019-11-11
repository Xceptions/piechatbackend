from django.contrib import admin
from appbackend.models import Account
from .models import Chats

admin.site.register(Account)
admin.site.register(Chats)