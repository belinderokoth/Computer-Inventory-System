from django.shortcuts import render,  redirect, get_object_or_404
from .models import Computer
from .forms import ComputerForm

# Create your views here.
# views.py

def computer_edit(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
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
        return redirect('list')
    context = {
        "title": title,
        "form": form,
        
    }
    return render(request, "computer_entry.html", context)


def computer_list(request):
    title = 'List of all computers'
    queryset = Computer.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list.html", context)

def computer_delete(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    instance.delete()
    return redirect("list")



