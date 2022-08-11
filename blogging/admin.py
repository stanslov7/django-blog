from django.contrib import admin
#from myblog.models import Post  # wrong import
from blogging.models import Post, Category  # <-- import Category

# Register your models here.
#admin.site.register(Post)  # and a new admin registration
#admin.site.register(Category)               # <-- Register Category as well

################################################
# Need to Register the models? --> Did it as 
# decorators + attached to relevant base model
###############################################
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
###############################################

# an InlineModelAdmin to represent Categories on the Post admin view
class CategoryInline(admin.TabularInline):  # or admin.StackedInline
    model = Category.posts.through
    # From the following line in models.py Category model class:
    # posts = models.ManyToManyField(Post, blank=True, related_name='categories')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # to represent Categories on the Post admin view
    inlines = [
        CategoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # to exclude the ‘posts’ field from the form in your Category admin
    exclude = ('posts',)
    #exclude = [
    #    'posts',
    #]
