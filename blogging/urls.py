from django.urls import path
#=========================================================================
#from blogging.views import stub_view  # still keep this for the detail_view part
#=========================================================================
# import the new view
from blogging.views import list_view, detail_view
# insert our new view into the existing blogging/urls.py in blogging:
#from blogging.views import detail_view

# and then update the urlconf
urlpatterns = [
    path('', 
        list_view,  #<-- Change this value from stub_view ('stub_view'-->'list_view')
        name="blog_index"),
    path('posts/<int:post_id>/', 
        detail_view, #<-- Change this from stub_view
        name="blog_detail"),  # This is the 'name' referred to in the url tag in detail view template
]                             # <!-- url template tag: {% url '<view_name>' arg1 arg2 %} -->

# Changed out stub, now that detail_view is ready in the same manner as list.html just before 