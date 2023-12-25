import requests
from django.shortcuts import redirect
from .requests_manager import Action
from frontend.settings import MAIN_URL

def login_required (function) : 

    def wrapper (request, **kwargs) : 

        user = request.COOKIES.get('user',None)

        if user is None :
            return redirect('login')
        
        action = Action(
            url = MAIN_URL + '/user/profile/',
            headers = {'Authorization':f"Bearer {user}"}
        )

        action.get()

        if not action.is_valid() : 
            return redirect('login')



        func = function(request,**kwargs)
        return func
    
    return wrapper


