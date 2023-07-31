from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.crear,name='home'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('votacion',views.votacion,name='votacion'),
    path('votacion/crear',views.crear,name='crear'),
    path('votacion/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('votacion/editar/<int:id>',views.editar,name='editar'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
