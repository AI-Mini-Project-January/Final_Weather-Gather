from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'identi', 
        'nickname', 
        'age',
        'profile_image'
        )
    search_fields = ('identi', 'nickname', 'age','profile_image')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) # Admin페이지의 GROUP삭제