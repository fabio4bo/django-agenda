from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact

from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )
    def clean(self):  # access to the data before saving.
        cleaned_data = self.cleaned_data
        # print(cleaned_data)

        self.add_error(
            'first_name',
            ValidationError(
                'Error Message',
                code='invalid'
            )
        )
        self.add_error(
            None,  # non_field_errors
            ValidationError(
                'Error Message',
                code='invalid'
            )
        )
        return super().clean()


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
    else:
        context = {
            'form': ContactForm()  # empty
        }
    print(request.method)
    return render(request, 'contact/create.html', context)
