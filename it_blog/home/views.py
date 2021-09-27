from django.shortcuts import render


def home_page(reqest):
    return render(reqest, 'home.html', {})