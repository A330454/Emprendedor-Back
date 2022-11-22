from django.contrib import admin
from django.urls import path, include
from jueces.views import login,hola,subjects
from rest_framework.routers import DefaultRouter
from jueces import views as JuecesViews
from rest_framework.urlpatterns import format_suffix_patterns 
from equipos import views as EquposViews

router_equipos = DefaultRouter()
router_equipos.register(r'noEvaluados', EquposViews.EquiposSinEvaluarViewSet)
router_equipos.register(r'evaluados', EquposViews.EquiposEvaluadosViewSet)
router_equipos.register(r'todos', EquposViews.TodosLosEquiposViewSet)
router_equipos.register(r'calificaciones', EquposViews.TodosLosEquiposCalificacionesViewSet)
router_equipos.register(r'nombres', EquposViews.TodosLosEquiposNombresViewSet)
router_equipos.register(r'ganadores/', EquposViews.EquiposGanadoresViewSet)
router_equipos.register(r'ganadores/calificaciones', EquposViews.CalificacionEquiposGanadoresViewSet)
router_equipos.register(r'ganadores/nombres', EquposViews.NombreEquiposGanadoresViewSet)
router_equipos.register(r'adminEquipos', EquposViews.TablaAdminEquiposGanadoresViewSet)
router_equipos.register(r'relacion', EquposViews.RelacionViewSet)

router_jueces = DefaultRouter()
router_jueces.register(r'', JuecesViews.viewset)
router_jueces.register(r'individual', JuecesViews.viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", login),
    path("graficas/", EquposViews.graficaPastel1),
    path("equipos/",include(router_equipos.urls)),
    path("jueces/",include(router_jueces.urls)),
    path("relacionByJuez/<id>/",EquposViews.get_relacion_by_juez),
    path("relacionByEquipo/<id>/",EquposViews.get_relacion_by_equipo)
    # path("unaRelacion/<id>/",EquposViews.get_1_relacion)
]
