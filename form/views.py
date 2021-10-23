from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from form.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, phone=phone, email=email,
                          message=message, date=datetime.today())
        contact.save()
        # messages.success(request, 'Your message has been sent!')

    return render(request, 'index.html')
    # return HttpResponse('this is contact page')
