from django.contrib import admin
from django.urls import path

from draw.view_digit import digits

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('digit/', digits, name='digit'),
]

