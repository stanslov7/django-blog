from django.urls import path
from blogging.views import stub_view  # still keep this for the detail_view part
# import the new view
from blogging.views import list_view

# and then update the urlconf
urlpatterns = [
    path('', 
        list_view,  #<-- Change this value from stub_view ('stub_view'-->'list_view')
        name="blog_index"),
    path('posts/<int:post_id>/', stub_view, name="blog_detail"),  # Added this in lesson 07
]   # will change the stub_view here when detail_view is ready in the same manner. 