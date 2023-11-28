# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactListForm
from .models import ContactList

def create_contactlist(request):
    if request.method == 'POST':
        form = ContactListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactListForm()

    return render(request, 'myapp3/create_contactlist.html', {'form': form})

def contactlist_list(request):
    if request.method == 'POST':
        contactlist_id_to_delete = request.POST.get('contactlist_id_to_delete')
        contactlist = ContactList.objects.get(id=contactlist_id_to_delete)
        contactlist.delete()
        return redirect('contactlist_list')

    contactlists = ContactList.objects.all()
    return render(request, 'myapp3/contactlist_list.html', {'contactlists': contactlists})


def delete_contactlist(request, contactlist_id):
    contactlist = get_object_or_404(ContactList, id=contactlist_id)

    try:
        if not contactlist.can_delete():
            raise Exception("Cannot delete contact because the expired date is 1 year away from the joined date.")

        contactlist.delete()
        return redirect('contactlist_list')
    except Exception as e:
        return render(request, 'myapp3/delete_error.html', {'error_message': str(e)})


def edit_contactlist(request, contactlist_id):
    contactlist = get_object_or_404(ContactList, id=contactlist_id)

    if request.method == 'POST':
        form = ContactListForm(request.POST, instance=contactlist)
        if form.is_valid():
            form.save()
            return redirect('contactlist_list')
    else:
        form = ContactListForm(instance=contactlist)

    return render(request, 'myapp3/edit_contactlist.html', {'form': form})


def success(request):
    return render(request, 'myapp3/success.html')