
from __future__ import unicode_literals
import bcrypt
from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import User

#
#
#
#   Registration and Validation area
#
#
#


def index(request):
    print 'Inside the the index method'  # print inside the terminal to check anything happening here
    return render(request, 'exam/index.html')


def create(request):
    print 'Inside the the CREATE method'
    if request.method == "POST":
        print ('*' * 50)
        print request.POST
        print ('*' * 50)
        form_data = request.POST
        check = User.objects.validate(form_data)

        if check:
            print check
            return redirect('/')

        password = str(form_data['password'])  # convert password to string
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())  # hash the password

        # INSERT into database
        user = User.objects.create(
            fname=form_data['fname'],
            lname=form_data['lname'],
            email=form_data['email'],
            dob=form_data['dob'],
            password=hashed_pw

        )  # saving feilds to the database including hashed password.

        request.session['user_id'] = user.id
        return redirect('/')

    return redirect('/')


def login(request):
    print "Inside the login method."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.login(form_data)  # sends to User to check validity

        if type(check) == type(User()):

            return redirect('/success')

        print check

    return redirect('/')


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


def success(request):
    return render(request, 'exam/success.html')


def result(arg):
    pass


def users(arg):
    pass


def books(request):

    if 'user_id' in request.session:
        user_id = request.session['user_id']

        context = {
            'user': User.objects.get(id=user_id)
        }

        return render(request, 'exam/success.html', context)

    return redirect('/books')  # send you back to the index page
