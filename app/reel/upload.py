from django.shortcuts import render
from globals.decorators import login_required

@login_required
def upload_reel (request) : 
    respones = render(request,'reel/upload.html')
    return respones
