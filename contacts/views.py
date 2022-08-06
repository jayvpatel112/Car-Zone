from django.shortcuts import render, redirect
from . models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method == "POST":
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        customer_need = request.POST["customer_need"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        # used to check if user already sent inquire for this car or not
        if request.user.is_authenticated:
            # user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id = car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquire for this car")
                return redirect('/cars/' + car_id)

        contact = Contact(car_id=car_id, car_title=car_title, customer_need=customer_need, user_id=user_id, first_name=first_name, last_name=last_name, city=city, state=state, email=email, phone=phone, message=message)

        # to get super user email id
        # admin_info =User.objects.get(is_superuser = True)
        # admin_email = admin_info.email
        

        send_mail(
                'New car inquiry',
                'You have new car inquire for the car' + car_title + 'Pleast login to your admin panel for more information',
                'pateljay.india@gmail.com',
                ['19bcscs028@student.rru.ac.in'],
                fail_silently=False,
            )        
        
        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you soon')
    return redirect('/cars/' + car_id)