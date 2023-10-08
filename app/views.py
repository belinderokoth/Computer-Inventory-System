from django.shortcuts import render,  redirect, get_object_or_404
from .models import Computer
from django.contrib import messages
from django.http import HttpResponse
import csv


from .forms import *

# Create your views here.
# views.py

def computer_edit(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, "updated successfully")
        return redirect('list')

    context = {
        "title": 'Edit ' + str(instance.computer_name),
        "instance": instance,
        "form": form,
    }
    return render(request, "computer_entry.html", context)

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
	"title": title,
	}
    return render(request, "home.html",context)


def computer_entry(request):
    title = 'Add Computer'
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('list')
    context = {
        "title": title,
        "form": form,
        
    }
    return render(request, "computer_entry.html", context)

def add_os(request):
    title = 'Add Operating System'
    form = OSForm()
    context={
        'form':form
    }
    if request.method == 'POST':
        form = OSForm(request.POST)
        if form.is_valid():
            form.save()
            form.save_m2m()
            messages.success(request, 'Successfully Saved')
            return redirect('computer_entry')
    return render(request, "add_os.html", context)


def computer_list(request):
    title = 'List of all computers'
    queryset = Computer.objects.all()
    form = ComputerSearchForm()

    if request.method == 'POST' :
        form = ComputerSearchForm(request.POST or None)
        queryset = Computer.objects.filter(
            computer_name__icontains=form['computer_name'].value(),
            users_name__icontains=form['users_name'].value(),
            
        )

    if form['export_to_CSV'].value() == True:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
        writer = csv.writer(response)
        writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
        instance = queryset

        for row in instance:
            writer.writerow([row.computer_name,       
            row.IP_address, row.MAC_address, row.users_name, row.location, row.purchase_date, row.timestamp])
        return response
        

    context = {
            "title": title,
            "queryset": queryset,
            "form":form
        }

    return render(request, "list.html", context)

def computer_delete(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    instance.delete()
    return redirect("list")
