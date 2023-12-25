from django.shortcuts import render, redirect
from globals.decorators import login_required
from globals.requests_manager import Action
from frontend.settings import MAIN_URL

@login_required
def upload_reel (request) : 
    context = {}
    if request.method == "POST" : 
        print(request.POST)
        data = {
            "x" : request.POST['x'],
            "y" : request.POST['y'],
            "font_size" : request.POST['font_size'],
            'verse' : request.POST['verse'],
        }


        scale = request.POST['scale']
        scale =  f'1.{scale}'
        
        if scale == '10': 
            scale = '2'
        
        data['scale'] = scale
            
        files = {
            'img' : request.FILES['image']
        }


        action = Action(
            url = MAIN_URL + "/reel/create/",
            headers = {"Authorization":f"Bearer {request.COOKIES.get('user')}"},
            data = data,
            files = files
        )

        action.post()

        if action.is_valid() :
            return redirect('home')
        else:
            print(action.json_data())
            context['error'] = 'توجد مشاكل في الرفع'


    return render(request,'reel/upload.html',context)
