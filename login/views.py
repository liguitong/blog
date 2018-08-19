from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import  render
from django.shortcuts import redirect

def index(request):
    return render(request,'login/index.html')
def validateuser(request):
    email = request.POST.get("email")
    print(email)
    password = request.POST.get('password')
    print(password)
    if password !='123':
        return redirect('%s?next=%s' % ('index', 'login/validateuser'))
    return HttpResponse("Hello,you login in to this site!")