from django.shortcuts import render

def upload_reel (request) : 
    respones = render(request,'reel/upload.html')
    return respones
