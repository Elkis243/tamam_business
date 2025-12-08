from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.views.decorators.http import require_http_methods
import os


def home(request):
    """Vue pour la page d'accueil"""
    context = {"page": "Home"}
    return render(request, "app/index.html", context)


def about(request):
    """Vue pour la page À propos"""
    context = {"page": "About"}
    return render(request, "app/about.html", context)


def services(request):
    """Vue pour la page Services"""
    context = {"page": "Services"}
    return render(request, "app/services.html", context)


def products(request):
    """Vue pour la page Produits"""
    context = {"page": "Products"}
    return render(request, "app/products.html", context)


def contact(request):
    """Vue pour la page Contact"""
    context = {"page": "Contact"}

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            # Ici vous pouvez ajouter l'envoi d'email ou sauvegarder en base de données
            # Exemple d'envoi d'email (nécessite configuration SMTP dans settings)
            try:
                if hasattr(settings, "EMAIL_BACKEND") and settings.EMAIL_BACKEND:
                    send_mail(
                        subject=f"Contact depuis le site - {name}",
                        message=f"Nom: {name}\nEmail: {email}\nTéléphone: {phone}\n\nMessage:\n{message}",
                        from_email=getattr(settings, "DEFAULT_FROM_EMAIL", email),
                        recipient_list=[
                            getattr(
                                settings, "CONTACT_EMAIL", "papymvulazana@gmail.com"
                            )
                        ],
                        fail_silently=True,
                    )
                messages.success(
                    request,
                    "Votre message a été envoyé avec succès. Nous vous répondrons dans les plus brefs délais.",
                )
            except Exception as e:
                # En mode développement, on accepte quand même le message
                messages.success(
                    request,
                    "Votre message a été reçu. Nous vous répondrons dans les plus brefs délais.",
                )

            return redirect("contact")
        else:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")

    return render(request, "app/contact.html", context)


@require_http_methods(["GET"])
def robots_txt(request):
    """Vue pour servir robots.txt"""
    from pathlib import Path

    base_dir = Path(settings.BASE_DIR)
    robots_path = base_dir / "tamam_business" / "static" / "robots.txt"

    if robots_path.exists():
        try:
            with open(robots_path, "rb") as f:
                return HttpResponse(f.read(), content_type="text/plain")
        except Exception:
            pass

    # Fallback si le fichier n'existe pas
    robots_content = """# robots.txt pour Tamam Business
# https://tamam.pythonanywhere.com/robots.txt

User-agent: *
Allow: /

# Bloquer les pages d'administration et autres pages sensibles
Disallow: /admin/
Disallow: /static/admin/
Disallow: /media/
Disallow: /*.json$

# Autoriser explicitement le sitemap
Allow: /sitemap.xml
Allow: /robots.txt

# Sitemap
Sitemap: https://tamam.pythonanywhere.com/sitemap.xml"""
    return HttpResponse(robots_content, content_type="text/plain")


@require_http_methods(["GET"])
def sitemap_xml(request):
    """Vue pour servir sitemap.xml"""
    from pathlib import Path

    base_dir = Path(settings.BASE_DIR)
    sitemap_path = base_dir / "tamam_business" / "static" / "sitemap.xml"

    if sitemap_path.exists():
        try:
            with open(sitemap_path, "rb") as f:
                return HttpResponse(f.read(), content_type="application/xml")
        except Exception:
            pass

    # Fallback si le fichier n'existe pas
    return HttpResponse(
        '<?xml version="1.0" encoding="UTF-8"?><urlset></urlset>',
        content_type="application/xml",
    )


@require_http_methods(["GET"])
def manifest_json(request):
    """Vue pour servir site.webmanifest"""
    from pathlib import Path
    import json

    base_dir = Path(settings.BASE_DIR)
    manifest_path = base_dir / "tamam_business" / "static" / "site.webmanifest"

    if manifest_path.exists():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest_data = json.load(f)
                # Mettre à jour les URLs avec le domaine actuel
                host = request.get_host()
                protocol = "https" if request.is_secure() else "http"
                base_url = f"{protocol}://{host}"
                
                # Mettre à jour les chemins des icônes avec le domaine complet
                for icon in manifest_data.get("icons", []):
                    src = icon.get("src", "")
                    if src.startswith("/static/"):
                        icon["src"] = f"{base_url}{src}"
                    elif not src.startswith("http"):
                        # Si le chemin est relatif, ajouter le domaine
                        icon["src"] = f"{base_url}/static/images/{src.split('/')[-1]}"
                
                return HttpResponse(
                    json.dumps(manifest_data, ensure_ascii=False, indent=2),
                    content_type="application/manifest+json",
                )
        except Exception as e:
            pass

    # Fallback si le fichier n'existe pas
    fallback_manifest = {
        "name": "Tamam Business",
        "short_name": "Tamam Business",
        "theme_color": "#667eea",
        "background_color": "#764ba2",
        "display": "standalone",
        "start_url": "/",
    }
    return HttpResponse(
        json.dumps(fallback_manifest, ensure_ascii=False, indent=2),
        content_type="application/manifest+json",
    )


# Handlers pour les pages d'erreur personnalisées
def bad_request(request, exception):
    """Handler pour l'erreur 400"""
    return render(request, "400.html", status=400)


def permission_denied(request, exception):
    """Handler pour l'erreur 403"""
    return render(request, "403.html", status=403)


def page_not_found(request, exception):
    """Handler pour l'erreur 404"""
    return render(request, "404.html", status=404)


def server_error(request):
    """Handler pour l'erreur 500"""
    return render(request, "500.html", status=500)
