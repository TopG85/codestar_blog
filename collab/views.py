from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CollaborateForm


def request_collab(request):
    if request.method == 'POST':
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks — your collaboration request has been sent.')
            return redirect('collab:request')
    else:
        form = CollaborateForm()
    return render(request, 'collab/request.html', {'form': form})
