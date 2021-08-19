from django.core import mail
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from validate_email import validate_email



def index(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        context = {
            "values":request.POST
        }

        if not name:
            messages.error(request, 'Name is required please')
            return render(request, 'index.html', context)
        
        if not email:
            messages.error(request, 'email is required please')
            return render(request, 'index.html', context)
        
        if not subject:
            messages.error(request, 'subject is required please')
            return render(request, 'index.html', context)
        
        if not message:
            messages.error(request, 'message is required please')
            return render(request, 'index.html', context)

        if not validate_email(email):
            messages.error(request, 'please enter a valid email')
            return render(request, 'index.html', context)

        senders_message = f'You have a message from {email}\n {message}'
        
        return redirect('thanks')

    return render(request, 'index.html')


def thanks(request):
    return render(request, 'thanks.html')