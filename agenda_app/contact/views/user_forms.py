from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    messages.info(request, 'Any text.')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully registered.')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        },
    )


def login_view(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            print(user)

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        },
    )
