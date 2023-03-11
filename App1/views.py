from django.shortcuts import render

# Create your views here.

def Sample(request):
    return render(request,'Sample.html')

def Sample3(request):
    return render(request,'Sample3.html')