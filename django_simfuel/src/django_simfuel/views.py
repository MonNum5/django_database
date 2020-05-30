from django.shortcuts import render

def navBarUserName(request):   
    if request.user.is_authenticated:
        userName = request.user.username
    else:
        userName = 'Sign In'
    context = {'username':userName}
    return context

def homePage(request):
    userInfo = navBarUserName(request)
    context = userInfo
    return render(request, 'homepage.html', context)