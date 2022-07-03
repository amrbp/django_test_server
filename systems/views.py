from django.shortcuts import render
from .forms import *
from systems.models import *

# Create your views here.


def home(request):
    return render(request, "routers/about.html")


def projects(request):
    s_form = Contact.objects.all()

    context = {
        's_form': s_form,
    }
    return render(request, "routers/projects.html", context)


def contact(request):
    p_form = ContactForm()
    if 'submit_p_form' in request.POST:
        p_form = ContactForm(request.POST)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.save()
            p_form = ContactForm()

    context = {
        'p_form': p_form,
    }

    return render(request, "routers/contact.html", context)
