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


def quote(request):
    """Vue pour la page Demander un devis"""
    context = {"page": "Quote"}

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and phone:
            try:
                if hasattr(settings, "EMAIL_BACKEND") and settings.EMAIL_BACKEND:
                    send_mail(
                        subject=f"Demande de devis - {name}",
                        message=f"Nom: {name}\nEmail: {email}\nTéléphone: {phone}\nService: {service}\n\nMessage:\n{message}",
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
                    "Votre demande de devis a été envoyée avec succès. Nous vous contacterons rapidement.",
                )
            except Exception as e:
                # En mode développement, on accepte quand même la demande
                messages.success(
                    request,
                    "Votre demande de devis a été reçue. Nous vous contacterons rapidement.",
                )

            return redirect("quote")
        else:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")

    return render(request, "app/quote.html", context)


def legal_notice(request):
    """Vue pour la page Mentions légales"""
    context = {"page": "Legal"}
    return render(request, "app/legal.html", context)


def privacy_policy(request):
    """Vue pour la page Politique de confidentialité"""
    context = {"page": "Privacy"}
    return render(request, "app/privacy.html", context)


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
    robots_content = """User-agent: *
Allow: /
Disallow: /admin/
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
