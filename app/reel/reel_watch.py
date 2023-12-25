from django.shortcuts import render
from globals.decorators import login_required


@login_required
def reel (request, reeluuid) :
    response = render(request,'reel/reel.html')
    return response