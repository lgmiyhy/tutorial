from django.shortcuts import render, HttpResponse

def home(request):
#    return HttpResponse('Home Page!!!')
    return render(request, 'accounts/login.html')
