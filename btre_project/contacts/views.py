from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact  # Import the Contact model

from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':       
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


        #check if user has made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing")
            return redirect('/listings/' + listing_id)
        

       
        # Save the contact inquiry to the database
        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        contact.save()         
        #send mail
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
            'kenkimosop6@gmail.com',
            [realtor_email, 'kenkimosop93@gmail.com'],
            fail_silently=False
        )
       


        # Display a success message
        messages.success(request, 'Your inquiry has been submitted, a realtor will get back to you soon.')

        # Redirect to the listing page
        return redirect('/listings/' + listing_id)

    else:
        # If the request method is not POST, redirect to the home page or show an error message
        messages.error(request, 'There was an error submitting your inquiry. Please try again.')
        return redirect('/')