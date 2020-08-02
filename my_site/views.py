from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm
import datetime, time, threading
tasks = []

def worker():
    send_mail(
            subject,
            message,
            'puchkovm@gmail.com',
            [to_email],
            fail_silently=False,
            )

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            threads = []
            start = form.cleaned_data['count']
            t = threading.Timer(start, worker)
            threads.append(t)
            t.start()
            subject = form.cleaned_data['subject']
            to_email = form.cleaned_data['To_email']
            message = form.cleaned_data['message']
            tasks.append({"text": message, "timer": t})
            time.sleep(start)
            send_mail(
            subject,
            message,
            'puchkovm@gmail.com',
            [to_email],
            fail_silently=False,
            )
        return HttpResponseRedirect('/thanks')
    else:
        form = ContactForm()
        return render(request, 'index.html', {'form': form})

def send(request):
    r = range(10)
    k = {}
    for x in r:
        k[x]=tasks
    return render(request, 'list.html', {'tasks':tasks})