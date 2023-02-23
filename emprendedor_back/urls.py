from django.contrib import admin
from django.urls import path, include
from jueces.views import login,hola,subjects
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns 
from jueces import views as JuecesViews
from equipos import views as EquposViews

from django.conf import settings
from django.conf.urls.static import static 

# GENETIC VIEWSETS "Equipos"
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
router_equipos.register(r'maestro-asesor', EquposViews.MaestroAsesorViewSet)

# GENETIC VIEWSETS "Jueces"
router_jueces = DefaultRouter()
router_jueces.register(r'', JuecesViews.viewset)
router_jueces.register(r'individual', JuecesViews.viewset)

router_admin = DefaultRouter()
router_admin.register(r'', JuecesViews.SuperUserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", login),
    path("graficas/", EquposViews.graficaPastel1),
    path("equipos/",include(router_equipos.urls)),
    path("jueces/",include(router_jueces.urls)),
    path("admins/",include(router_admin.urls)),
    path("relacionByJuez/<id>/",EquposViews.get_relacion_by_juez),
    path("relacionByJuezNull/<id>/",EquposViews.get_relacion_null_by_juez),
    path("relacionByEquipo/<id>/",EquposViews.get_relacion_by_equipo),
    path("relaciones/calificadas/<id>/",EquposViews.cuenta_relacionones_calificadas_by_equipo),
    path("relaciones/output/<id>/",EquposViews.relacionones_calificadas_by_equipo),
    path('userByToken/<token>/',JuecesViews.token_a_user),

    # Class as APIView
    path("eliminarEquipos/",EquposViews.EliminarEquipos.as_view()),
    path("eliminarRelaciones/",EquposViews.EliminarRelaciones.as_view())

    # path("endpoint/",EquposViews.get_cal_equip)
    # path("unaRelacion/<id>/",EquposViews.get_1_relacion)
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
