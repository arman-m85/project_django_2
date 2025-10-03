from django.contrib import admin
from users.models  import admin_user,profile

# Register your models here.

admin.site.register(admin_user)
admin.site.register(profile)