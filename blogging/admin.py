from django.contrib import admin
#from myblog.models import Post  # wrong import
from blogging.models import Post, Category  # <-- import Category

# Register your models here.

admin.site.register(Post)  # and a new admin registration
admin.site.register(Category)               # <-- Register Category as well