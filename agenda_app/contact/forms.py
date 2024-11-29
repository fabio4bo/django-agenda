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
            attrs={
                'class': 'class-a class-b',
                'placeholder': 'I didn\'t come from models.',
            }
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
            'email',
            'description',
            'category',
        )

    def clean(self):  # access to the data before saving.
        cleaned_data = self.cleaned_data
        # print(cleaned_data)

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'last_name',
                ValidationError(
                    'Last name can\'t be equal to first name.', code='invalid'
                ),
            )

        # self.add_error('first_name', ValidationError('Error Message 1', code='invalid'))
        # self.add_error(
        #     None, ValidationError('Error Message: non_field', code='invalid')  # non_field_errors
        # )
        return super().clean()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if last_name == 'ABC':
            self.add_error(
                'last_name',
                ValidationError('I\'m from add_error! clean_last_name', code='invalid'),
            )

        return last_name
