from django.contrib import admin
from .models import UserInfo


class UserInfoSort(admin.ModelAdmin):
    list_filter = ['city']


admin.site.register(UserInfo, UserInfoSort)
