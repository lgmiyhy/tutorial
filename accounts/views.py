from django.shortcuts import render, HttpResponse

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Max Goodridge'
    args = {'myName':name, 'numbers':numbers}
#    return HttpResponse('Home Page!!!')
    return render(request, 'accounts/login.html', args)
