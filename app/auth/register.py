from django.shortcuts import render

def register (request) :
    response = render(request,'auth/register.html')

    return response