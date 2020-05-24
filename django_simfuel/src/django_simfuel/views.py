from django.shortcuts import render

def navBarUserName(request):   
    if request.user.is_authenticated:
        userName = request.user.username
    else:
        userName = 'Guest'
    context = {'username':userName}
    return context