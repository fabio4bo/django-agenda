from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'class-a class-b', 'placeholder': 'First name.'}
        ),
        label='Your First Name:',
    )
    new_widget = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'class-a class-b', 'placeholder': 'I didn\'t come from models.'}
        ),
        label='I am a new widget:',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs.update(
            {  # html
                'class': 'class-a class-b',
                'placeholder': 'Phone. This is from a widget using __init__.',
            }
        )

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self):  # access to the data before saving.
        # cleaned_data = self.cleaned_data
        # print(cleaned_data)

        self.add_error('first_name', ValidationError('Error Message', code='invalid'))
        self.add_error(
            None, ValidationError('Error Message', code='invalid')  # non_field_errors
        )
        return super().clean()