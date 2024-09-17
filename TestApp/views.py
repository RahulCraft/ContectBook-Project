from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from .models import Contact
from django.shortcuts import render,redirect


from django.shortcuts import render, redirect
from .models import Contact

# View for saving new contact
def add_contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        # Create a new Contact object and save it
        new_contact = Contact(firstname=firstname, lastname=lastname, email=email, contact_number=phone)
        new_contact.save()
        return redirect('index')  # After saving, redirect to the page showing all contacts
    return render(request, 'add_contact.html')

# View for displaying all contacts
def index(request):
    Data = Contact.objects.all()
    return render(request,"index.html",{'Data':Data})

def formupdate(request, id):
    # Get the Contact object by id
    contact = Contact.objects.get(id=id)
    
    if request.method == "POST":
        # Update fields from form data
        contact.firstname = request.POST.get("firstname")
        contact.lastname = request.POST.get("lastname")
        contact.email = request.POST.get("email")
        contact.contact_number = request.POST.get("phone")
        
        # Save the updated object back to the database
        contact.save()

        # Redirect to index after saving
        return redirect("index")
    
    # If GET request, render the edit form with existing data
    return render(request, 'edit.html', {'Data': contact})


def edit(request,id):
        Data = Contact.objects.get(id=id)
        return render(request,'edit.html',{'Data':Data})

def delete(request,id):
        add = Contact.objects.get(id=id)
        add.delete()
        return redirect('index')


def contact_list(request):
    # Retrieve all contacts and pass to template
    contacts = Contact.objects.all()  # Assuming you have a Contact model
    return render(request, 'contact_list.html', {'Data': contacts})



def search_contacts(request):
    query = request.GET.get('query', '')  # Get the search query
    if query:
        # Search for both first name and last name
        results = Contact.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query)
        )
    else:
        results = Contact.objects.none()  # No results if no query
    return render(request, 'contact_list.html', {'contacts': results})