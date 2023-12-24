from django.shortcuts import render

def login (request) :
    respones =  render(request,'auth/login.html')

    return respones