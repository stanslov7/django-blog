"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Made sure to add imports of both django.url methods used
# add an import at the top
from django.contrib.auth.views import LoginView, LogoutView

# modified first line of urlpatterns as follows:
# and update the list of urlconfs
urlpatterns = [
    path('', include('blogging.urls')),  # <-- Added this in lesson 07
    path('polling/', include('polling.urls')),  # <-- Added this in lesson 06
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),  # new
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),            # new
]
