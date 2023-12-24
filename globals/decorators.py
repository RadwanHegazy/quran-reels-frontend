import requests



def login_required (function) : 

    def wrapper (request) : 
        func = function(request)
        return func
    
    return wrapper


