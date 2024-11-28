from django.shortcuts import render

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        context = {'form': ContactForm(request.POST)}
    else:
        context = {'form': ContactForm()}  # empty; GET
    print(request.method)
    return render(request, 'contact/create.html', context)
