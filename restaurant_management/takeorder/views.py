from django.shortcuts import render
from.models import Tables
def takeorder(request):
    data = {
        "tables": Tables.objects.all(),
    }
    return render(request, "index.html",data)
def takeorder(request):
    return render(request, "take_order.html" )
