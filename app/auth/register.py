from django.shortcuts import render, redirect
from globals.requests_manager import Action
from frontend.settings import MAIN_URL


def register (request) :
    context = {}
    if request.method == "POST" : 

        data = {
            'picture' : None
        }

        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        data['full_name'] = full_name
        data['email'] = email
        data['password'] = password

        if 'picture' in request.FILES :
            picture = request.FILES['picture']
            data['picture'] = picture

        action = Action(
            url = MAIN_URL + '/user/register/',
            data = data,
            files={
                'picture' : data['picture']
            }
        )

        action.post()

        if action.is_valid() :
            token = action.json_data()['access']
            response = redirect('home')
            response.set_cookie('user',token)
            return response
        else :
            context['error'] = "توجد مشكلة في انشاء حساب"

        
    

    return render(request,'auth/register.html', context)