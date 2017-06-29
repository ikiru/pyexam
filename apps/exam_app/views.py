
from __future__ import unicode_literals
import bcrypt
from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import User
from django.contrib import messages

#
#
#
#  flash messages area
#
#
#


def dash_flash(request, errors):
    messages.success(request, "Sucessful Registation")


def error_flash(request, errors):
    for error in errors:
        messages.error(request, error)


def login_flash(request, errors):
    messages.error(request, "User is not in the Database")

#
#
#
#   Registration and Validation area
#
#
#


def index(request):
    # print inside the terminal to check anything happening here
    print 'Inside the the index method'
    return render(request, 'exam/index.html')


def create(request):
    print 'Inside the the CREATE method'
    if request.method == "POST":
        form_data = request.POST
        check = User.objects.validate(form_data)

        if check != []:
            error_flash(request, check)
            return redirect('/')
        # valid form data
        password = str(form_data['password'])  # convert password to string
        hashed_pw = bcrypt.hashpw(
            password, bcrypt.gensalt())  # hash the password

        user = User.objects.create(
            name=form_data['name'],
            username=form_data['username'],
            email=form_data['email'],
            password=hashed_pw

        )  # saving feilds to the database including hashed password.

        request.session['user_id'] = user.id
        dash_flash(request, check)
        return redirect('/')

#
#
# Sucessful login page
#
#
#


def login(request):
    print "Inside the login method."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.validate_login(form_data)  # calls vaidate method

        if check:
            print check
            # login_flash(request, check)
            return redirect('/')

        User.objects.login(form_data)
        return redirect('/dash')

    return redirect('/')


def dash(request):
    print 'inside the dash method'
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        queryset = Trip.objects.get()

        context = {
            'user': User.objects.get(id=user_id),
            'trip': queryset,
            "destination": "list",
        }

        return render(request, 'exam/dash.html', context)

    return redirect('/')  # send you back to the index page


#
#
# Sucessful logout page
#
#
#


def logout(request):
    request.session.pop('user_id')  # pop the value in the session variable

    return redirect('/')  # send you back to the index page


#
#
#
#
#    Specific Application area below
#
#
#
#

def trip(request):  # add id
    ######## multiple file ###########
    queryset = trip.objects.get(session.id)
    context = {
        'trip': queryset,
        "destination": "list"
    }

    return render(request, 'exam/dash.html', context)


def other(request,):
    queryset = trip.objects.all().exclude(session.id)
    context = {
        'user': queryset,
        "destination": "list"
    }

    return render(request, 'exam/dash.html', context)

    ######## single file ###########
    # instance = get_object_or_404(table. id=id)
    # context = {
    #     'object_list' = queryset, blank in blanks
    #     'title': 'list'
    # }
    # on html page instance.title


def add(request):

    return render(request, 'exam/add.html')


def result(request):

    return render(request, 'exam/result.html')


def add_trip(request):
    if request.method == "POST":
        form_data = request.POST
        check = Trip.validate_trip(form_data)

        if check != []:
            error_flash(request, check)
            return redirect('/')

        user = Trip.objects.create(
            destination=form_data['destination'],
            description=form_data['description'],
            start_d=form_data['start_d'],
            end_d=form_data['end_d'],
            user=session.id
        )  # saving feilds to the database

    return render(request, 'exam/dash.html')
