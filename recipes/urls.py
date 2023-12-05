

from django.contrib import admin
from django.urls import path
from food.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , food_recipes, name="recipes"),
    path('delete_recipes/<id>/', delete_recipes, name='delete_recipes'),
    path('update_recipes/<id>/', update_recipes, name='update_recipes'),
    path('login', login_page, name= 'login'),
    path('register', register_page, name= 'register')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
