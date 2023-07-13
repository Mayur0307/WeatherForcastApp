from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def weatherPage(request):
    return render(request,'mainpage.html')
