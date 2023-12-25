from django.shortcuts import render
from globals.decorators import login_required
from globals.requests_manager import Action
from frontend.settings import MAIN_URL
from django.http import Http404

@login_required
def reel (request, reeluuid) :
    
    context = {}

    action = Action(
        url = MAIN_URL + f'/reel/retrive/{reeluuid}/',
        headers = {'Authorization':f'Bearer {request.COOKIES.get("user")}'},
    )

    action.get()

    if action.is_valid() :
        context['reel'] = action.json_data()
    else : 
        raise Http404(request)
    
    return render(request,'reel/reel.html',context)