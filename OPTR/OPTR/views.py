from django.shortcuts import render

def home(request):
    return render(request,'home.html',locals())

#test branch
def bracnhtest(request):
    return render(request,'home.html',locals())
