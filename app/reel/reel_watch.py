from django.shortcuts import render

def reel (request, reeluuid) :
    response = render(request,'reel/reel.html')
    return response