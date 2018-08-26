from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import  render
from django.shortcuts import redirect

def index(request):
    return render(request,'login/login.html')
def welcome(request):
    email = request.POST.get("email")
    password = request.POST.get('password')
    if not validate(password):
        return redirect('%s?next=%s' % ('index', 'login/welcome'))
    #return HttpResponse("Hello,you login in to this site!")
    return render(request, 'index.html')
def validate(user):
    if user !='123':
        return False
    else:
        return True