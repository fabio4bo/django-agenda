from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
        }

    print(contacts.query)

    # paginator = Paginator(contacts, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # context = {'page_obj': page_obj, 'site_title': 'Contatos - '}

    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    # get - único
    # filter - queryset
    # single_contact = Contact.objects.get(pk=contact_id)
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True))  # AND
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)  # AND

    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': contact_name,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
