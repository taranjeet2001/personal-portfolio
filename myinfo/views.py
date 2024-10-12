from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
def view_home(request):
    if request.method == 'GET':
        return render(request,'myinfo/home.html')

@csrf_exempt
def view_save_data(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        usr = contact(name = name, email = email , subject = subject , message = message)
        usr.save()
        #    stud = User.objects.values()
        #    print(stud)
        #    student_data = list(stud)
        return JsonResponse({'status':'Save'})
    except:
        return JsonResponse({'status':0})