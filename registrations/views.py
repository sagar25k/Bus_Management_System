from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm
from .models import Registration


def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registrations/registration_list.html', {'registrations': registrations})


def registration_details(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    return render(request, 'registrations/registration_details.html', {'registration': registration})


@login_required
def registration_create(request):
    if not request.user.profile.user_type in ['admin','student','incharge']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('registration_list')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration created successfully!')
            return redirect('registration_list')
    else:
        form = RegistrationForm()
    
    return render(request, 'registrations/registration_form.html', {'form': form})


@login_required
def registration_update(request, pk):
    if not request.user.profile.user_type in ['admin','student','incharge']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('registration_list')
    
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration updated successfully!')
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=registration)
    
    return render(request, 'registrations/registration_form.html', {'form': form})


@login_required
def registration_delete(request, pk):
    if not request.user.profile.user_type in ['admin']:
        messages.error(request, 'You do not have admin permission to access this page.')
        return redirect('registration_list')
    
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        registration.delete()
        messages.success(request, 'Registration deleted successfully!')
        return redirect('registration_list')
    
    return render(request, 'registrations/registration_confirm_delete.html', {'registration': registration})
