from django.shortcuts import render
from globals.decorators import login_required
from globals.requests_manager import Action
from frontend.settings import MAIN_URL

@login_required
def home_reels (request) :
    context = {}
    action = Action(
        url = MAIN_URL + "/reel/get/",
        headers = {"Authorization":f"Bearer {request.COOKIES.get('user')}"}
    )

    action.get()
    context['reels'] = action.json_data()
    
    return render(request,'home.html',context)
