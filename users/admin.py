from django.contrib import admin
from users.models  import Author, admin_user, book,profile

# Register your models here.

admin.site.register(admin_user)
admin.site.register(profile)
admin.site.register(book)
admin.site.register(Author)