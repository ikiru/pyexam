from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.db import models
from .models import *
from django.core.urlresolvers import reverse
import bcrypt

#
#
#
#
#
# Validation of the Registation
#
#
#
#
#


class Usermanager(models.Manager):
    def validate(self, form_data):
        errors = []  # arrary where we will store the error messages

        if len(form_data['name']) == 0 and len(form_data['name']) > 3:
            # check if name is blank
            errors.append("Name is required and must be at least 3 characters")

        if len(form_data['username']) == 0 and len(form_data['username']) > 3:
            # check if username is blank
            errors.append(
                "User Name is required and must be at least 3 characters.")

        if len(form_data['email']) == 0:
            errors.append("email required.")  # check if email is blank

        if len(form_data['password']) == 00 and len(form_data['password']) > 3:
            # check if password is blank
            errors.append(
                "Password is required and must be at least 3 characters.")

        if len(form_data['cpassword']) == 0:
            # check if cpassword is blank
            errors.append("Comfirm Password is required.")

        if form_data['cpassword'] != form_data['password']:
            # check if password and confirm password match
            errors.append("Passwords much match")

        return errors  # send error messages to the form page
#
#
#
#
#
# Validation of the login
#
#
#
#
#
#

    def validate_login(self, form_data):

        errors = []  # define error array

        if len(form_data['email']) == 0:
            errors.append("email required.")  # check if email is blank

        if len(form_data['password']) == 0:
            errors.append("Password is required.")  # check if pasword is blank

        return errors

    def login(self, form_data):
        print 'inside login model'
        errors = self.validate_login(form_data)

        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

            if user:
                # turn password in to string
                password = str(form_data['password'])
                user_password = str(user.password)
                # hash the password with bcrypt
                hashed_pw = bcrypt.hashpw(password, user_password)
                print user_password
                print hashed_pw
                if hashed_pw == user_password:  # compare hashed password with user entered password
                    return user

            # append any errors to array
            errors.append('Invalid Account Information')

        return errors  # return errors to views
#
#
#
#
# USER model and validation
#
#
#
#


class User(models.Model):

    # create name field as a string type field
    name = models.CharField(max_length=255)
    # create username field as a string type field
    username = models.CharField(max_length=255)
    # create email field as a string type field
    email = models.CharField(max_length=255)
    # create password field as an encrypted field
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("result", kwarg={"id": self.id})

# show whats is going on in the console
    def __str__(self):
        string_output = "id:{} name:{} username:{} email{} password{}"
        return string.output.format(
            self.id,
            self.name,
            self.username,
            self.email,
            self.password
        )

    objects = Usermanager()

#
#
#
#
# TRIP model and validation
#
#
#
#


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    users = models.ManyToManyField(User,  related_name="trip")
    start_d = models.DateField('%d %b %Y')
    end_d = models.DateField('%d %b %Y')
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} destination:{} description:{} start_d{} end_d{}"
        return string.output.format(
            self.id,
            self.destination,
            self.description,
            self.start_d,
            self.end_d
        )

        objects = validate_trip()


class Join(models.Model):
    joined = models.ForeignKey(User, related_name="joiner")
    joiner = models.ForeignKey(User, related_name="joined")
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)


#
#
#
#
# trip model and validation
#
#
#
#

def validate_trip(self, form_data):
    errors = []
    if len(form_data['destination']) == 0:
        # check if email is blank
        errors.append("A destination is is required.")

    if len(form_data['description']) == 0:
        # check if pasword is blank
        errors.append("A description is is required.")

    if 'end_d' < 'start_d':
        # check if pasword is blank
        errors.append("End date cannot be before start date")

    return errors


# class Book(models.Model):  # create Book model
#
#     # create created_at field as a one time Date type field
#     created_at = models.DateTimeField(auto_now_add=True)
#     # create updated_at field as a updated on change Date type field
#     updated_at = models.DateTimeField(auto_now=True)


# class Bookmanager(models.Manager):
#     def book(self, form_data):
#         errors = []  # define error array
#
#         if len(form_data['title']) == 0:
#             errors.append("title required.")  # check if email is blank
#
#         if len(form_data['review']) == 0:
#             errors.append("Password is required.")  # check if pasword is blank
#
#         return errors

#
#
#
#
# Author model and validation
#
#
#
#


# class Author(models.Model):
#     name = models.TextField(max_length=255)
#     # FK for Book One author can have many books
#     book = models.ForeignKey(Book)


# class Authormanager(models.Manager):
#     def book(self, form_data):
#         errors = []  # define error array
#
#         if len(form_data['title']) == 0:
#             errors.append("title required.")  # check if email is blank
#
#         if len(form_data['rev']) == 0:
#             errors.append("Password is required.")  # check if pasword is blank
#
#         return errors
