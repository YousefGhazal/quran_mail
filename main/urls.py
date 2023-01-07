from django.urls import path
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Quran_mail API",
        default_version='v1'
    ),
    public=True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/',views.contact, name='contact'),
    path('unsubscribe/<str:id>/',views.unsubscribe, name='unsubscribe'),
]
