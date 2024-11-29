from django.shortcuts import render

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form}

        if form.is_valid():  # without errors
            form.save()
    else:
        context = {'form': ContactForm()}  # empty; GET
    print(request.method)
    return render(request, 'contact/create.html', context)
