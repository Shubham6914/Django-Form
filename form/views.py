# views.py

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm
from.models import Registration
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Form is Submitted..!")
            return redirect('show')
        else:
            print("Form has validation errors:", form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'form/form.html', {'form': form})


def show_data(request):
    registrations = Registration.objects.all()
    print(registrations)  # Check the console or terminal for this output
    return render(request, 'form/showdata.html', {'registrations': registrations})



# def Update_view(request, id):
#     if request.method == 'POST':
#         user = Registration.objects.get(pk=id)
#         form = RegistrationForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('update_registration', kwargs={'id': user.id}))
#     else:
#         user = Registration.objects.get(pk=id)
#         form = RegistrationForm(instance=user)

#     return render(request, 'form/update.html', {'form': form})
def Update_view(request, id):
    if request.method == 'POST':
        # If the form is submitted, populate it with the request data and the instance data
        user = Registration.objects.get(pk=id)
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('show')  # Redirect to the show_data view after successful update
    else:
        # If it's a GET request, render the form with the current data
        user = Registration.objects.get(pk=id)
        form = RegistrationForm(instance=user)

    return render(request, 'form/update.html', {'form': form, 'registration': user})


def delete_registration(request, id):
    if request.method == 'POST':
        registration = Registration.objects.get(pk=id)
        registration.delete()
        return redirect('show')  # Redirect to the show_data view after successful deletion

# ...