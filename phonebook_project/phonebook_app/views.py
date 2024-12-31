from django.shortcuts import render, get_object_or_404, redirect
from .models import phonebook

# Home page
def home(request):
        phone_list = phonebook.objects.all()

        # Render the HTML template with the data
        return render(request, "index.html", {'phone_list': phone_list})
# Add phone number
def addphonenumber(request):
    response_dict = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')

            # Check if phone number already exists
            if phonebook.objects.filter(name=name).exists():
                response_dict["message"] = "Phone number already exists for this name."
            else:
                phonebook.objects.create(name=name, phone=phone)
                response_dict["message"] = "Phone number added successfully."

            # Redirect to displaylist to show updated list
            return redirect('displaylist')

    except Exception as e:
        print(f"Error adding phone number: {e}")
        response_dict["message"] = "An error occurred while adding the phone number."
        return render(request, "index.html", response_dict)

# Display phonebook entries
def displaylist(request):
    try:
        # Fetch all phonebook entries from the database
        phone_list = phonebook.objects.all()

        # Render the HTML template with the data
        return render(request, "index.html", {'phone_list': phone_list})
    except Exception as e:
        print(f"Error fetching phonebook data: {e}")
        return render(request, "index.html", {'message': "Failed to load phonebook entries."})

def deletephone(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')  # The name to delete

            # Find the phonebook entry by name
            phone_entry = phonebook.objects.filter(name=name).first()

            if phone_entry:
                # Delete the phonebook entry if found
                phone_entry.delete()
                return redirect('displaylist')  # Redirect to the phonebook list page
            else:
                return render(request, "index.html", {'message': "Phonebook entry with this name not found."})

    except Exception as e:
        print(f"Error deleting phone number: {e}")
        return render(request, "index.html", {'message': "An error occurred while deleting the phone number."})

# Update phonebook entry
def updatename(request):
    try:
        if request.method == 'POST':
            old_name = request.POST.get('name')  # The old name to find the entry
            new_name = request.POST.get('newname')  # The new name to update with

            # Find the phonebook entry using the old name
            phone_entry = phonebook.objects.filter(name=old_name).first()

            if phone_entry:
                # Update the name if the entry exists
                phone_entry.name = new_name
                phone_entry.save()
                # Redirect to displaylist to show updated list
                return redirect('displaylist')
            else:
                return render(request, "index.html", {'message': "Phonebook entry not found."})

    except Exception as e:
        print(f"Error updating name: {e}")
        return render(request, "index.html", {'message': "An error occurred while updating the name."})
