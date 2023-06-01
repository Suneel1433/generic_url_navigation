from django.shortcuts import render

# Create your views here.
def senior(request):
    return render(request,'senior.html')

def junior(request):
    return render(request,'junior.html')