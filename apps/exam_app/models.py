
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.db import models
import bcrypt
#
#
#
#
#
#Validation of the Registation
#
#
#
#
#

class Usermanager(models.Manager):
    def validate(self,form_data):
        errors=[]  #arrary where we will store the error messages

        if len(form_data['fname']) == 0:
            errors.append("First Name is required.") #check if fname is blank

        if len(form_data['lname']) == 0:
            errors.append("Last Name is required.") #check if lname is blank

        if len(form_data['email']) == 0:
            errors.append("email required.") #check if email is blank

        if len(form_data['dob']) == 0:
            errors.append("Date of birth required.") #check if DOB is blank

        if len(form_data['password']) == 0:
            errors.append("Password is required.") #check if password is blank

        if len(form_data['cpassword']) == 0:
            errors.append("Comfirm Password is required.") #check if cpassword is blank

        if form_data['cpassword'] != form_data['password']:
            errors.append("Passwords much match") #check if password and confirm password match

        return errors #send error messages to the form page



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
        errors=[] #define error array

        if len(form_data['email']) == 0:
            errors.append("email required.") #check if email is blank

        if len(form_data['password']) == 0:
            errors.append("Password is required.") #check if pasword is blank

        return errors

    def login(self,form_data):
        errors = self.validate_login(form_data)

        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

            if user:
                password = str(form_data['password']) #turn password in to string
                user_password = str(user.password)
                hashed_pw = bcrypt.hashpw(password, user_password) #hash the password with bcrypt

                print user.password
                print hashed_pw

                if hashed_pw == user_password: #compare hashed password with user entered password
                    return user

            errors.append('Invalid Account Information') #append any errors to array

        return errors #return errors to views



class User(models.Model):

    fname = models.CharField(max_length=255) #create fname field as a string type field
    lname = models.CharField(max_length=255) #create lname field as a string type field
    email = models.CharField(max_length=255) #create email field as a string type field
    password = models.CharField(max_length=255) #create password field as an encrypted field
    dob = models.DateField()# creates DateField
    created_at = models.DateTimeField(auto_now_add=True) #create created_at field as a one time Date type field
    updated_at = models.DateTimeField(auto_now=True) #create updated_at field as a updated on change Date type field

#built in string method
    def __str__(self):
        string_output = "id:{} fname:{} lname:{} email{} password{}"
        return string.output.format(
        self.id,
        self.fname,
        self.lname,
        self.email,
        self.password
    )

    objects = Usermanager()

#
#
#
#
# Book model and validation
#
#
#
#

class Book(models.Model): #create Book model

    title = models.CharField(max_length=255) #create title field as a string type field
    created_at = models.DateTimeField(auto_now_add=True) #create created_at field as a one time Date type field
    updated_at = models.DateTimeField(auto_now=True) #create updated_at field as a updated on change Date type field


class Bookmanager(models.Manager):
    def book(self, form_data):
        errors=[] #define error array

        if len(form_data['title']) == 0:
            errors.append("title required.") #check if email is blank

        if len(form_data['review']) == 0:
            errors.append("Password is required.") #check if pasword is blank

        return errors

#
#
#
#
# Author model and validation
#
#
#
#



class Author(models.Model):
    name = models.TextField(max_length = 255) #
    book = models.ForeignKey(Book) #FK for Book One author can have many books



class Authormanager(models.Manager):
    def book(self, form_data):
        errors=[] #define error array

        if len(form_data['title']) == 0:
            errors.append("title required.") #check if email is blank

        if len(form_data['rev']) == 0:
            errors.append("Password is required.") #check if pasword is blank

        return errors
