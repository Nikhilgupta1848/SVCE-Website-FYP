from django.contrib import admin
from service.models import Contact
from django.contrib.auth.admin import UserAdmin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'add')
admin.site.register(Contact, ContactAdmin)

class BookinfoAdmin(admin.ModelAdmin):
    list_display=('bookname','sem_year', 'link')
admin.site.register(Bookinfo, BookinfoAdmin)
