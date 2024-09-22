from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def HomeView(request):
    about_us = About_us.objects.all().order_by('-id')
    carousel = Carousel.objects.all().order_by('-id')
    twitter = Twitter.objects.all().order_by('-id')
    statistic = Statistic.objects.all().order_by('-id')
    context = {'about_us': about_us, 'carousel': carousel, 'twitter': twitter, 'statistic': statistic}
    return render(request, 'index.html', context)


def phasedes(request, study_id):
    stu = Study_Details.objects.filter(study_id=study_id)
    context = {'stu': stu}
    return render(request, 'phase_details.html', context)


def about(request):
    about_us = About_us.objects.all().order_by('-id')
    context = {'about_us': about_us}
    return render(request, 'about.html', context)


def main_gallery(request, study_id):
    stu = News.objects.filter(study_id=study_id)
    galleries = Gallery.objects.filter(study_id=study_id)
    vid = Videos.objects.filter(study_id=study_id)
    context = {'study_id': study_id, 'stu': stu, 'galleries': galleries, 'vid': vid}
    return render(request, 'main_gallery.html', context)


def study(request):
    stu = Study.objects.all()
    context = {'stu': stu}
    return render(request, 'study.html', context)


def institute_news(request, study_id):
    new = News.objects.filter(study_id=study_id)
    context = {'new': new}
    return render(request, 'Institute_news.html', context)


def gallery(request, study_id):
    galleries = Gallery.objects.filter(study_id=study_id)
    context = {'galleries': galleries}
    return render(request, 'gallery.html', context)


def videos(request, study_id):
    vid = Videos.objects.filter(study_id=study_id)
    context = {'vid': vid}
    return render(request, 'video.html', context)


def document(request):
    doc = Documents.objects.all()
    context = {'doc': doc}
    return render(request, 'document.html', context)


def team(request):
    team_member = Team.objects.all()
    idrone_team = Idrone_Team.objects.all()
    research_team = Research_Techanical_Team.objects.all()
    admin_team = Admin_IT_Team.objects.all()
    context = {'team_member': team_member,
               'idrone_team': idrone_team,
               'admin_team': admin_team,
               'research_team': research_team,
               }
    return render(request, 'team.html', context)


def institute(request):
    inst = Institute.objects.all()
    context = {'inst': inst}
    return render(request, 'Institute.html', context)



def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        has_error = False

        # Validate the input data
        if not name.isalpha():
            messages.error(request, "Please enter a valid name. Only letters are allowed.")
            has_error = True

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address.")
            has_error = True

        if not phone.isdigit() or not (5 <= len(phone) <= 15):
            messages.error(request, "Please enter a valid phone number (5 to 15 digits).")
            has_error = True

        if not (1 <= len(message) <= 1000):
            messages.error(request, "Please enter a valid message (up to 1000 characters).")
            has_error = True

        # If any validation errors, render the form with error messages
        if has_error:
            return render(request, 'contact.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
                'error_messages': messages.get_messages(request)
            })

        # If all validations pass, save the data
        data = Contact_us(name=name, email=email, phone=phone, message=message)
        data.save()
        messages.success(request,
                         "Thank you for contacting us! We have received your message and will get back to you as soon as possible.")
        return redirect("contact")

    return render(request, 'contact.html')


def study_complete(request):
    stu = Study.objects.filter(status='Completed').order_by('id')
    context = {'stu': stu}
    return render(request, 'study_complete.html', context)


def study_ongoing(request):
    stu = Study.objects.filter(status='Ongoing').order_by('id')
    context = {'stu': stu}
    return render(request, 'study_ongoing.html', context)
