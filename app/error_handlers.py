"""
Custom error handlers for better security and user experience.
These handlers prevent information leakage and provide user-friendly error pages.
"""

import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger(__name__)


def handler400(request, exception=None):
    """
    Handler for 400 Bad Request errors.
    Returns a custom 400 error page without exposing sensitive information.
    Logs the error for debugging without exposing details to users.
    """
    # Log error details for debugging (only in development or with proper logging)
    if settings.DEBUG and exception:
        logger.warning(f"400 Bad Request: {exception}", exc_info=True)
    else:
        logger.warning("400 Bad Request: Invalid request received")

    # Return generic error page without exposing exception details
    return render(request, "400.html", status=400)


def handler403(request, exception=None):
    """
    Handler for 403 Forbidden errors.
    Returns a custom 403 error page without exposing sensitive information.
    """
    # Log error details for debugging
    if settings.DEBUG and exception:
        logger.warning(f"403 Forbidden: {exception}", exc_info=True)
    else:
        logger.warning("403 Forbidden: Access denied")

    # Return generic error page without exposing exception details
    return render(request, "403.html", status=403)


def handler404(request, exception=None):
    """
    Handler for 404 Not Found errors.
    Returns a custom 404 error page without exposing sensitive information.
    """
    # Log the requested path for debugging (not the full exception)
    path = request.path if hasattr(request, "path") else "unknown"
    logger.info(f"404 Not Found: {path}")

    # Return generic error page without exposing exception details
    return render(request, "404.html", status=404)


def handler500(request):
    """
    Handler for 500 Internal Server Error.
    Returns a custom 500 error page without exposing sensitive information.
    This handler does not receive an exception parameter.
    Logs the error for administrators.
    """
    # Log the error for administrators
    logger.error("500 Internal Server Error", exc_info=True)

    # Return generic error page without exposing any technical details
    return render(request, "500.html", status=500)
