from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs.update(
            {  # html
                'class': 'class-a class-b',
                'placeholder': 'Phone. This is from a widget using __init__.',
            }
        )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
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
            'picture',
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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            'required': 'I change the required message. This is still required.'
        },
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'This email is already being used.',
                ),
            )
