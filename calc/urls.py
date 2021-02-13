from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('calc/', views.calc, name='calc'),
    path('sub/', views.sub, name='sub'),
    path('secret/', views.secret, name='secret'),
    path('secsub/', views.secsub, name='secsub'),  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)