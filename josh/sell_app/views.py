from django.shortcuts import render, get_object_or_404

from .models import Outfit, Category

# Create your views here.

def detail(request,pk):
    item = get_object_or_404(Outfit, pk=pk)
    #Outfit is the table to be searched
    related_items = Outfit.objects.filter(category = item.category, is_bought=False).exclude(pk=pk)[0:1]
    return render(request, "more_data/detail.html", {
        "item":item,
        "related_items":related_items
    })