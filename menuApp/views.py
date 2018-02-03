from django.shortcuts import render
from .models import MenuOption
from .forms import MenuForm

def index(request):

    # object = MenuOption(title="Patryk")
    # object.save()
    return render(request, 'index.html')

def dane(request):

    menuOptions = MenuOption.objects.all()[:10]

    context = {
        'menuOptions': menuOptions
    }

    return render(request, 'dane.html', context)

def fill_form(request):

    return render(request, 'add.html')

def add_user_to_database(request):

    title = 'unknown user'

    if request.method == "POST":
        NewUser = MenuForm(request.POST)

        if NewUser.is_valid():
            title = NewUser.cleaned_data['title']
            insertUser = MenuOption(title=title)
            insertUser.save()
    else:
        NewUser = MenuForm()

    return render(request, 'index.html')


