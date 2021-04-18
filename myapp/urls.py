from django.urls import path, include
from .views import home
from django.conf.urls.static import static
from django.conf import settings
app_name = 'myapp'
urlpatterns = [
    path('', home,name='home'),
    
] 