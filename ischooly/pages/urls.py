from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
"""
urlpatterns = [
    path('', views.java),
    path('<str:filename>/', views.python),
#    path('java/<str:folder>/<str:files>', views.java, name='java'),
]
"""
urlpatterns = [
    path('', views.home, name='home'),
    path('Python/item1', views.item1, name='item1'),
    path('Python/item2', views.item2, name='item2'),
    path('Python/item3', views.item3, name='item3'),
    path('Java/item1', views.jitem1, name='jitem1'),
    path('Java/item2', views.jitem2, name='jitem2'),
    path('Java/item3', views.jitem3, name='jitem3'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)