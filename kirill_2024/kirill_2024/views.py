from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'gretting': 'Reverse!'})


def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request, 'reverse.html', {'word': reverse})
