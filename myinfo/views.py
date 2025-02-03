from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import *


# Create your views here.
def view_home(request):
    if request.method == 'GET':
        return render(request,'myinfo/home.html')

@csrf_exempt
def send_contact_email(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Using EmailMessage (allows better formatting)
            email_message = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,
                to=['taranjeetsingh999928@gmail.com'],  # Change to the email where you want to receive messages
                reply_to=[email],  # Allows you to reply directly to the sender
            )
            email_message.send()

            return JsonResponse({'status': 'Sent'})
        except Exception as e:
            return JsonResponse({'status': 'Error', 'message': str(e)})

    return JsonResponse({'status': 'Invalid request'}, status=400)








# @csrf_exempt
# def view_save_data(request):
#     try:
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         usr = contact(name = name, email = email , subject = subject , message = message)
#         usr.save()
#         #    stud = User.objects.values()
#         #    print(stud)
#         #    student_data = list(stud)
#         return JsonResponse({'status':'Save'})
#     except:
#         return JsonResponse({'status':0})