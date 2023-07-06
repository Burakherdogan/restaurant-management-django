from django.shortcuts import render
from.models import Tables, Category
def index_view(request):
    data = {
        "tables": Tables.objects.all(),
    }
    return render(request, "index.html",data)
def takeorder(request):
    data = {
        "category": Category.objects.all(),
    }
    return render(request, "take_order.html",data)
