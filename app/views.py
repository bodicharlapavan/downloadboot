from django.shortcuts import render

# Create your views here.


def downloadboot(request):
    return render(request, 'downloadboot.html')
