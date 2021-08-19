from django.core import mail
from django.shortcuts import render
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
        
        try:
            send_mail(
                subject,
                senders_message,
                email,
                ['hrfunsojoba@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Mail sent, thank you')
            return render(request, 'index.html')
        except Exception as err:
            messages.error(request, f'Something went wrong: {err}')
            return render(request, 'index.html')
    return render(request, 'index.html')
