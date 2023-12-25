from django.shortcuts import render, redirect
from globals.requests_manager import Action
from frontend.settings import MAIN_URL

def login (request) :
    context = {}

    if request.method == "POST" : 
        data = {
            'email' : request.POST['email'],
            'password' : request.POST['password'],
        }  
        
        action = Action(
            url = MAIN_URL + '/user/login/',
            data = data
        )

        action.post()

        if action.is_valid() : 
            response = redirect('home')
            token = action.json_data()['access']
            response.set_cookie('user',token)
            return response
        else:
            context['error'] = 'البيانات التي ادخلتها خاطئة'


    return render(request,'auth/login.html', context)