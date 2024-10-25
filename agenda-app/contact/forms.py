from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    # Forma 3
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Seu Telefone",
            }
        ),
        label="Telemóvel",  # sobrepõe o do model
        help_text="Telemóvel? É português agora?",  # deve adicionar no html
    )

    um_novo_campo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                # melhor usar classe de acordo com o css
                "style": "background-color:#00a489; font-size:16px; color:white",
                "placeholder": "Texto de exemplo.",
            }
        ),
        label="Descrição:",
    )

    # Forma 2
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["last_name"].widget.attrs.update(
            {
                "class": "classe-a classe-b",
                "placeholder": "Seu último nome",
            }
        )

    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )
        # Forma 1
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "classe-a classe-b",
                    "placeholder": "Seu primeiro nome",
                }
            ),
            "email": forms.EmailInput(attrs={"placeholder": "exemplo@email.com.br"}),
        }

    def clean(self):  # manipula antes de salvar
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     "first_name", ValidationError("Mensagem de erro", code="invalid")
        # )
        # self.add_error(
        #     "first_name", ValidationError("Mensagem de erro 2", code="invalid")
        # )

        return super().clean()

    # clean por campo
    def clean_um_novo_campo(self):
        um_novo_campo = self.cleaned_data.get("um_novo_campo")

        if um_novo_campo == "Vasco":
            print("Time da virada")
        else:
            self.add_error(
                "um_novo_campo",
                ValidationError("Vasco. Veio do add_error", code="invalid"),
            )
        return um_novo_campo
