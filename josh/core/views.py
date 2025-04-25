from django.shortcuts import render, redirect, get_object_or_404
from hire_app.models import Category, Outfit
from sell_app.models import Category as C, Outfit as O
from .forms import SignupForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from sell_app.models import Outfit as SellOutfit
from hire_app.models import Outfit as HireOutfit
from .forms import SearchForm, MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    categories = Category.objects.all
    gender = C.objects.all
    type = O.objects.filter(is_bought = False)[0:5]
    outfits = Outfit.objects.filter(is_hired = False)[0:5]
    return render(request, "index.html",{
        "gender":gender,
        "type":type,
       "categories":categories,
       "outfits":outfits

    })



@login_required
def inbox(request):
    messages = Message.objects.all().order_by('-timestamp')  # Retrieve messages
    return render(request, 'inbox.html', {'messages': messages})


def contact(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)

    else:
        form = MessageForm()
    

    return render(request, "contact.html", {
        'form': form
    })


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        else:
            form =SignupForm()
            return redirect('/signup/', {
                "form":form
            })

    else:
        form = SignupForm()
    

    return render(request, "signup.html", {
        'form': form
    })

def browse(request):
    form = SearchForm()
    sell_results = []
    hire_results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            sell_results = SellOutfit.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            hire_results = HireOutfit.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search_results.html', {
        'form': form,
        'sell_results': sell_results,
        'hire_results': hire_results,
    })
