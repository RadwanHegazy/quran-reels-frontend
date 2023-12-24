from django.shortcuts import render

def home_reels (request) :
    response = render(request,'home.html')

    return response
