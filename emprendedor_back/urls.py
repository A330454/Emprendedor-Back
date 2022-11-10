from django.contrib import admin
from django.urls import path, include
from jueces.views import login,hola,subjects
from rest_framework.routers import DefaultRouter
from jueces import views as JuecesViews
from rest_framework.urlpatterns import format_suffix_patterns 
from equipos import views as EquposViews

router = DefaultRouter()
router.register(r'noEvaluados', EquposViews.EquiposSinEvaluarViewSet)
router.register(r'evaluados', EquposViews.EquiposEvaluadosViewSet)
router.register(r'todos', EquposViews.TodosLosEquiposViewSet)
router.register(r'calificaciones', EquposViews.TodosLosEquiposCalificacionesViewSet)
router.register(r'nombres', EquposViews.TodosLosEquiposNombresViewSet)
router.register(r'ganadores/', EquposViews.EquiposGanadoresViewSet)
router.register(r'ganadores/calificaciones', EquposViews.CalificacionEquiposGanadoresViewSet)
router.register(r'ganadores/nombres', EquposViews.NombreEquiposGanadoresViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", login),
    #path("equipos/", views.EquipoList.as_view(), name="listar_equipos"),
    #path('jueces/', views.list_subjects, name="lista-subjects")
    path("graficas/", EquposViews.graficaPastel1),
    path("mushoOjoCuate/", EquposViews.eliminar_todos_los_equipos),
    path("equipos/",include(router.urls))
]
