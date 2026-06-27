from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

from .models import PortfolioProfile


def view_home(request):
    profile = (
        PortfolioProfile.objects.prefetch_related(
            "tags", "experiences", "certifications", "skills"
        ).first()
    )
    return render(request, "myinfo/home.html", {"profile": profile})


@csrf_exempt
def send_contact_email(request):
    if request.method == "POST":
        try:
            profile = PortfolioProfile.objects.first()
            recipient = profile.email if profile else settings.EMAIL_HOST_USER

            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            email_message = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[recipient],
                reply_to=[email],
            )
            email_message.send()

            return JsonResponse({"status": "Sent"})
        except Exception as e:
            return JsonResponse({"status": "Error", "message": str(e)})

    return JsonResponse({"status": "Invalid request"}, status=400)
