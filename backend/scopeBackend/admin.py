# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Query , User

class ScopeBackendAdmin(admin.ModelAdmin):
    #list_display = ('title', 'description', 'completed')
    list_display = ['id']

# Register your models here.
#admin.site.register(Query, ScopeBackendAdmin)
admin.site.register([Query, User], ScopeBackendAdmin)
