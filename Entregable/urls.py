from django.contrib import admin
from django.urls import path, include
from proyecto.views import  *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto/', include('proyecto.urls'))
]
