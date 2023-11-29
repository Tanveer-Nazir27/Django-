from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def mithu(request):
    return render(request,'abc.html')