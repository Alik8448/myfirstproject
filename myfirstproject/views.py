from django.shortcuts import render
def about(requests):
    return render(requests, 'home.html', {'greeting':'hi'})