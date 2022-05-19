from django.contrib import admin

from .models import FbLogIn, NewLogs, SiteContent

# Register your models here.

admin.site.register(FbLogIn)
admin.site.register(NewLogs)
admin.site.register(SiteContent)
