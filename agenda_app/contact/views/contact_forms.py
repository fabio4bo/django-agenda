from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
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


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )  # don't forget the pk
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(
            request.POST, request.FILES, instance=contact
        )  # instance of contact that exists
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():  # without errors
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)  # contact.id
    else:
        context = {
            'form': ContactForm(instance=contact),  # empty; GET
            'form_action': form_action,
        }

    return render(request, 'contact/create.html', context)


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        },
    )
