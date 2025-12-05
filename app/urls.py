from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
    path("quote/", views.quote, name="quote"),
    path("legal/", views.legal_notice, name="legal"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("robots.txt", views.robots_txt, name="robots"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap"),
]
