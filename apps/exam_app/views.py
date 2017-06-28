
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


def success_flash(request, errors):
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
            fname=form_data['fname'],
            lname=form_data['lname'],
            email=form_data['email'],
            dob=form_data['dob'],
            password=hashed_pw

        )  # saving feilds to the database including hashed password.

        request.session['user_id'] = user.id
        success_flash(request, check)
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
        return redirect('/success')

    return redirect('/')


def success(request):
    print 'inside the success method'
    if 'user_id' in request.session:
        user_id = request.session['user_id']

        context = {
            'user': User.objects.get(id=user_id)
        }

        return render(request, 'exam/success.html', context)

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
def result(request):  # add id
    ######## multiple file ###########
    # queryset = Post.objects.all()
    # context = {
    #     'object_list' = queryset, blank in blanks
    #     'title': 'list'
    # }

    ######## single file ###########
    # instance = get_object_or_404(table. id=id)
    # context = {
    #     'object_list' = queryset, blank in blanks
    #     'title': 'list'
    # }
    # on html page instance.title

    return render(request, 'exam/result.html', context)


def add(request):

    return render(request, 'exam/add.html')

# def books(request):
#
#     if 'user_id' in request.session:
#         user_id = request.session['user_id']
#
#         context = {
#             'user': User.objects.get(id=user_id)
#         }
#
#         return render(request, 'exam/success.html', context)
#
#     return redirect('/books')  # send you back to the index page
