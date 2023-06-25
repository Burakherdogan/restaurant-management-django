from django.shortcuts import render

def takeorder(request):
    return render(request, "index.html")
