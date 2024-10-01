from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from config import settings
from django.conf.urls.i18n import set_language
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Saidoff API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('saidoff/', include('app.urls')),
                  path('set_language/', set_language, name='set_language'),
                  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
