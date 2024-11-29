from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():  # without errors
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)  # contact.id
    else:
        context = {
            'form': ContactForm(),  # empty; GET
            'form_action': form_action,
        }

    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)  # don't forget the pk
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)  # instance of contact that exists
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():  # without errors
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)  # contact.id
    else:
        context = {
            'form': ContactForm(instance=contact),  # empty; GET
            'form_action': form_action,
        }

    return render(request, 'contact/create.html', context)
