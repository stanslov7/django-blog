from django.contrib import admin
#from myblog.models import Post  # a new import
from blogging.models import Post  # a new import

# Register your models here.

admin.site.register(Post)  # and a new admin registration