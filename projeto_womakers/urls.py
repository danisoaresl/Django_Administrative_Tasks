
















from django.urls import path
from base.views import inicio, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cadastro/', cadastro),
    path('curso/, include('cursos.urls', namespace='cursos')),
]