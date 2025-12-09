from django.urls import path
from django.conf import settings
from . import views
from . import error_handlers

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
    path("robots.txt", views.robots_txt, name="robots"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap"),
    path("site.webmanifest", views.manifest_json, name="manifest"),
]

# Routes de test pour les pages d'erreur (uniquement en développement)
if settings.DEBUG:
    urlpatterns += [
        path("test-400/", lambda r: error_handlers.handler400(r, None)),
        path("test-403/", lambda r: error_handlers.handler403(r, None)),
        path("test-404/", lambda r: error_handlers.handler404(r, None)),
        path("test-500/", error_handlers.handler500),
    ]
